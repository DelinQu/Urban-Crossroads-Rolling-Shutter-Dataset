mkdir output
mkdir output/gs
mkdir output/rs

sudo docker run --rm --interactive \
  --user $(id -u):$(id -g)      \
  --volume "$(pwd):/kubric"     \
  kubricdockerhub/kubruntu      \
  /usr/bin/python3 rs/camera_para.py


############################ RS simulator ############################
seq=01
echo $seq
sudo docker run --rm --interactive \
  --user $(id -u):$(id -g)      \
  --volume "$(pwd):/kubric"     \
  kubricdockerhub/kubruntu      \
  /usr/bin/python3 rs/model.py  \
  --use_motion_blur=1           \
  --out_dir=output/rs/seq$seq/    \
  --pose=./rs/data/pose$seq.csv \
  --write=1

seq=02
echo $seq
sudo docker run --rm --interactive \
  --user $(id -u):$(id -g)      \
  --volume "$(pwd):/kubric"     \
  kubricdockerhub/kubruntu      \
  /usr/bin/python3 rs/model.py  \
  --use_motion_blur=1           \
  --out_dir=output/rs/seq$seq/    \
  --pose=./rs/data/pose$seq.csv \
  --write=1

seq=03
echo $seq
sudo docker run --rm --interactive \
  --user $(id -u):$(id -g)      \
  --volume "$(pwd):/kubric"     \
  kubricdockerhub/kubruntu      \
  /usr/bin/python3 rs/model.py  \
  --use_motion_blur=1           \
  --out_dir=output/rs/seq$seq/    \
  --pose=./rs/data/pose$seq.csv \
  --write=1

seq=04
echo $seq
sudo docker run --rm --interactive \
  --user $(id -u):$(id -g)      \
  --volume "$(pwd):/kubric"     \
  kubricdockerhub/kubruntu      \
  /usr/bin/python3 rs/model.py  \
  --use_motion_blur=1           \
  --out_dir=output/rs/seq$seq/    \
  --pose=./rs/data/pose$seq.csv \
  --write=1

seq=05
echo $seq
sudo docker run --rm --interactive \
  --user $(id -u):$(id -g)      \
  --volume "$(pwd):/kubric"     \
  kubricdockerhub/kubruntu      \
  /usr/bin/python3 rs/model.py  \
  --use_motion_blur=1           \
  --out_dir=output/rs/seq$seq/    \
  --pose=./rs/data/pose$seq.csv \
  --write=1

seq=06
echo $seq
sudo docker run --rm --interactive \
  --user $(id -u):$(id -g)      \
  --volume "$(pwd):/kubric"     \
  kubricdockerhub/kubruntu      \
  /usr/bin/python3 rs/model.py  \
  --use_motion_blur=1           \
  --out_dir=output/rs/seq$seq/    \
  --pose=./rs/data/pose$seq.csv \
  --write=1

seq=07
echo $seq
sudo docker run --rm --interactive \
  --user $(id -u):$(id -g)      \
  --volume "$(pwd):/kubric"     \
  kubricdockerhub/kubruntu      \
  /usr/bin/python3 rs/model.py  \
  --use_motion_blur=1           \
  --out_dir=output/rs/seq$seq/    \
  --pose=./rs/data/pose$seq.csv \
  --write=1

############################ GS simulator ############################
seq=01
echo $seq
sudo docker run --rm --interactive \
  --user $(id -u):$(id -g)      \
  --volume "$(pwd):/kubric"     \
  kubricdockerhub/kubruntu      \
  /usr/bin/python3 rs/model.py  \
  --use_motion_blur=0           \
  --out_dir=output/gs/seq$seq/    \
  --pose=./rs/data/pose$seq.csv \
  --write=1

seq=02
echo $seq
sudo docker run --rm --interactive \
  --user $(id -u):$(id -g)      \
  --volume "$(pwd):/kubric"     \
  kubricdockerhub/kubruntu      \
  /usr/bin/python3 rs/model.py  \
  --use_motion_blur=0           \
  --out_dir=output/gs/seq$seq/    \
  --pose=./rs/data/pose$seq.csv \
  --write=1

seq=03
echo $seq
sudo docker run --rm --interactive \
  --user $(id -u):$(id -g)      \
  --volume "$(pwd):/kubric"     \
  kubricdockerhub/kubruntu      \
  /usr/bin/python3 rs/model.py  \
  --use_motion_blur=0           \
  --out_dir=output/gs/seq$seq/    \
  --pose=./rs/data/pose$seq.csv \
  --write=1

seq=04
echo $seq
sudo docker run --rm --interactive \
  --user $(id -u):$(id -g)      \
  --volume "$(pwd):/kubric"     \
  kubricdockerhub/kubruntu      \
  /usr/bin/python3 rs/model.py  \
  --use_motion_blur=0           \
  --out_dir=output/gs/seq$seq/    \
  --pose=./rs/data/pose$seq.csv \
  --write=1

seq=05
echo $seq
sudo docker run --rm --interactive \
  --user $(id -u):$(id -g)      \
  --volume "$(pwd):/kubric"     \
  kubricdockerhub/kubruntu      \
  /usr/bin/python3 rs/model.py  \
  --use_motion_blur=0           \
  --out_dir=output/gs/seq$seq/    \
  --pose=./rs/data/pose$seq.csv \
  --write=1

seq=06
echo $seq
sudo docker run --rm --interactive \
  --user $(id -u):$(id -g)      \
  --volume "$(pwd):/kubric"     \
  kubricdockerhub/kubruntu      \
  /usr/bin/python3 rs/model.py  \
  --use_motion_blur=0           \
  --out_dir=output/gs/seq$seq/    \
  --pose=./rs/data/pose$seq.csv \
  --write=1

seq=07
echo $seq
sudo docker run --rm --interactive \
  --user $(id -u):$(id -g)      \
  --volume "$(pwd):/kubric"     \
  kubricdockerhub/kubruntu      \
  /usr/bin/python3 rs/model.py  \
  --use_motion_blur=0           \
  --out_dir=output/gs/seq$seq/    \
  --pose=./rs/data/pose$seq.csv \
  --write=1
