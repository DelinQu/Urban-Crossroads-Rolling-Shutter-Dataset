import numpy as np
from kubric.safeimport.bpy import bpy

import kubric as kb

bpy.context.scene.render.use_motion_blur = True
bpy.context.scene.cycles.motion_blur_position='CENTER'
bpy.context.scene.cycles.rolling_shutter_type = 'TOP'
bpy.context.scene.cycles.rolling_shutter_duration = 0.5
bpy.context.scene.render.motion_blur_shutter = 0.05


# ? create scene and attach a renderer and simulator
scene = kb.Scene(resolution=(640, 480))

# ! Create a camera and set pose.
scene.camera = kb.PerspectiveCamera(
    name="camera",
    position=(2, 2, 0.35),
    look_at=(2, 0, 0.35),
    # focal_length=35.,
    # sensor_width=32
)

width, height = scene.resolution
intrinsics = scene.camera.intrinsics * np.array([
    [width, 0, width],
    [0, height, height],
    [0, 0, 1]
])
print('intrinsics: \n {}, \n scene.resolution: \n {}'.format(np.abs(intrinsics), scene.resolution))