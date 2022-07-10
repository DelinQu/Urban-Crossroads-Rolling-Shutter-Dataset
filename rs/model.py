import argparse
import logging
import os

import kubric as kb
from kubric.renderer.blender import Blender as KubricBlender
from kubric.simulator.pybullet import PyBullet as KubricSimulator
import config
import copy
import pandas as pd
from kubric.safeimport.bpy import bpy

logging.basicConfig(level="INFO")
parser = argparse.ArgumentParser()
parser.add_argument("--num_frames", type=int, default=48)
parser.add_argument("--pose", type=str, default='./rs/data/pose01.csv')

parser.add_argument("--use_motion_blur", type=int, default=1)                   # default 0.1   |   Max 1.0, 
parser.add_argument("--rolling_shutter_type", type=str, default='TOP')          # ['TOP', 'NONE'] 
parser.add_argument("--rolling_shutter", type=float, default=0.05)              # default 0.05  |   Max 1.0, 
parser.add_argument("--motion_blur_shutter", type=float, default=0.5)           # default 0.5   |   Max 1.0,
parser.add_argument("--motion_blur_position", type=str, default='CENTER')       # default 0.5   |   Max 1.0,

parser.add_argument("--out_dir", type=str, default='./output')                  # dir
parser.add_argument('--write', type=int, default=0)

FLAGS = parser.parse_args()
print('FLAGS {}'.format(FLAGS))

# ? create scene and attach a renderer and simulator
scene = kb.Scene(resolution=(640, 480))
scene.frame_end = FLAGS.num_frames      # < numbers of frames to render
scene.frame_rate = 24                   # < rendering framerate
scene.step_rate = 240                   # < simulation framerate

renderer = KubricBlender(scene)         # Assign the renderer to the scene
simulator = KubricSimulator(scene)      # Assign the Simulator to the scene
kubasic = kb.AssetSource.from_manifest('gs://kubric-public/assets/KuBasic/KuBasic.json')
hdri_source = kb.AssetSource.from_manifest('gs://kubric-public/assets/HDRI_haven/HDRI_haven.json')
asset_source = kb.AssetSource.from_manifest('gs://kubric-unlisted/assets/ShapeNetCore.v2.json')


# ! Rolling Shutter
bpy.context.scene.render.use_motion_blur = FLAGS.use_motion_blur                                            # Turn on motion blur inside the Renderer
logging.info("Motion blur is turned on in the Scene Renderer, use_motion_blur: {}".format(FLAGS.use_motion_blur)) #loggy loggy log
bpy.context.scene.cycles.motion_blur_position=FLAGS.motion_blur_position
logging.info("Motion blur position is turned on the {} of the frame".format(FLAGS.motion_blur_position)) 
bpy.context.scene.cycles.rolling_shutter_type = FLAGS.rolling_shutter_type                                  # Now when we set this it will apply as the setting is on
logging.info(f"Rolling Shutter type is {bpy.context.scene.cycles.rolling_shutter_type}")                    #loggy loggy log
bpy.context.scene.cycles.rolling_shutter_duration = FLAGS.rolling_shutter                                   # Set the duration of the motion blur
logging.info(f"Rolling Shutter duration is {bpy.context.scene.cycles.rolling_shutter_duration}")            #loggy loggy log
bpy.context.scene.render.motion_blur_shutter = FLAGS.motion_blur_shutter                                    # Set the shutter speed of the motion blur
logging.info(f"Motion Blur Shutter speed is {bpy.context.scene.render.motion_blur_shutter}")                #loggy loggy log

# ! background HDRI
hdri_id = 'wide_street_01'
background_hdri = hdri_source.create(asset_id=hdri_id)
logging.info("Using background %s", hdri_id)
scene.metadata["background"] = hdri_id
renderer._set_ambient_light_hdri(background_hdri.filename)
dome = kubasic.create(asset_id="dome", name="dome",
                      friction=0.3,
                      restitution=0.5,
                      static=True, background=True)
assert isinstance(dome, kb.FileBasedObject)
scene += dome
dome_blender = dome.linked_objects[renderer]
texture_node = dome_blender.data.materials[0].node_tree.nodes["Image Texture"]
texture_node.image = bpy.data.images.load(background_hdri.filename)

# ! cars
# obj = asset_source.create(asset_id=config.cars['id'][0])
for i, id in enumerate(config.cars['id']):
    obj = asset_source.create(asset_id=config.cars['id'][i])
    obj.position = config.cars['position'][i]
    obj.scale = config.cars['scale'][i]
    q = config.cars['quat'][i]
    obj.quaternion = kb.Quaternion(w=q[0], z=q[1], y=q[2], x=q[3])
    # obj.static = True
    obj.velocity = config.cars['velocity'][i]
    obj.angular_velocity = (0,0,0)
    obj.friction = 0
    scene += copy.deepcopy(obj)

# ! buildings.
# obj = asset_source.create(asset_id=config.buildings['id'][1])
for i, id in enumerate(config.buildings['id']):
    obj = asset_source.create(asset_id=config.buildings['id'][i])
    obj.position = config.buildings['position'][i]
    obj.scale = config.buildings['scale'][i]
    q = config.buildings['quat'][i]
    obj.quaternion = kb.Quaternion(w=q[0], z=q[1], y=q[2], x=q[3])
    obj.static = True
    scene += copy.deepcopy(obj)

# ! lamps
obj = asset_source.create(asset_id=config.lamps['id'][0])
obj.position = config.lamps['position'][0]
obj.scale = config.lamps['scale'][0]
q = config.lamps['quat'][0]
obj.quaternion = kb.Quaternion(w=q[0], z=q[1], y=q[2], x=q[3])
for i, id in enumerate(config.lamps['id']):
    obj.position = config.lamps['position'][i]
    obj.static = True
    scene += copy.deepcopy(obj)

# ! Create a camera and set pose.
df = pd.read_csv(FLAGS.pose)
scene.camera = kb.PerspectiveCamera(
    name="camera",
    position=(2, 2, 0.35),
    look_at=(2, 0, 0.35),
    # focal_length=35.,
    # sensor_width=32
)

for i, frame in enumerate(range(scene.frame_start, scene.frame_end + 1)):
    scene.camera.position = (df.x[i], df.y[i], df.z[i])
    scene.camera.quaternion = kb.Quaternion(w=df.q_w[i], z=df.q_z[i], y=df.q_y[i], x=df.q_x[i])
    logging.info(
        'set camera pose x {} y {} z {}  trans {} {} {} {}'.format(df.x[i], df.y[i], df.z[i], df.q_w[i], df.q_z[i], df.q_y[i], df.q_x[i])
        )
    scene.camera.keyframe_insert("position", frame)
    scene.camera.keyframe_insert("quaternion", frame)

# ! executes the simulation (and store keyframes)
simulator.run()
out_dir = FLAGS.out_dir
os.makedirs(out_dir, exist_ok=True)
logging.info('makedir {}'.format(out_dir))
renderer.save_state(f"{out_dir}/model.blend")

# ! write to file
if FLAGS.write:
    frames_dict = renderer.render()
    frames_dict.pop('segmentation')
    frames_dict.pop('object_coordinates')
    frames_dict.pop('forward_flow')
    frames_dict.pop('backward_flow')
    frames_dict.pop('normal')
    frames_dict.pop('depth')

    # --- renders the output
    kb.write_image_dict(frames_dict, out_dir)
