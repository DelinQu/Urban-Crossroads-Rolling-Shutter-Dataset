# Urban-Crossroads-Rolling-Shutter-Dataset (UCR)

The world's first synthetic RS dataset for dynamic scene UCR (Urban Crossroads Rolling Shutter Dataset) based on Kubric: <https://github.com/google-research/kubric>. UCR contains seven challenging sequences with various strong dynamic objects and camera motions. It also provides the corresponding GS frames which have been captured at the intermediate exposure time of RS frames.

| ![CDR](https://user-images.githubusercontent.com/60593268/177999356-436726ab-f548-40f1-8f83-20c27ab82447.png) | ![CDR2](https://user-images.githubusercontent.com/60593268/177999378-6d0a09c9-a27f-4cdd-ac6d-57fa3c61f663.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

## Sequences

| id              | seq01                                                        | seq02                                                        | seq03                                                        | seq04                                                        | seq05                                                        | seq06                                                        | seq07                                                        |
| --------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **thumbnail**   | ![rgba_00001](https://user-images.githubusercontent.com/60593268/178001537-2c576377-05f2-4548-bb26-15625a232073.png) | ![rgba_00011](https://user-images.githubusercontent.com/60593268/178005126-acd19a2d-2885-4b93-8704-f8567fa4c831.png) | ![rgba_00001](https://user-images.githubusercontent.com/60593268/178005169-74679d74-0c98-4f49-97c8-544afff0beb9.png) | ![rgba_00021](https://user-images.githubusercontent.com/60593268/178005209-b7f10931-b499-41f3-a283-9fd1ffd60401.png) | ![rgba_00001](https://user-images.githubusercontent.com/60593268/178005248-624d7652-1436-4a77-92db-466131e3cacd.png) | ![rgba_00002](https://user-images.githubusercontent.com/60593268/178005392-0811eb68-b8c8-4443-9f36-63b4fe571ff6.png) | ![rgba_00006](https://user-images.githubusercontent.com/60593268/178005451-fc16d7ac-3a40-43aa-81d2-24a7448ed360.png) |
<!-- | **trajectory**  | |  | |  |  |  |  | -->
| **pose**        | pose01.txt                                                   | pose02.txt                                                   | pose03.txt                                                   | pose04.txt                                                   | pose05.txt                                                   | pose06.txt                                                   | pose07.txt                                                   |
| **description** | Fix camera                                                   | Fix camera                                                   | Translation                                                  | Sine curve                                                   | Rotate along the x axis                                      | Rotate along the y axis                                      | Half of the heart curve                                      |

## Camera

- instriction

```python
intrinsics: 
 [[888.88888889   0.         320.        ]
 [  0.         888.88888889 240.        ]
 [  0.           0.           1.        ]], 
```

- resolution

```python
resolution: 
(640, 480)
```

- shutter

```python
FPS: 24 Hz
exposure time: 1 / 24 * 0.05 s
time delay between two scanlines: 1 / 24 * 0.5 / 480 s
```

## Script

The render script is based on Kubric: <https://github.com/google-research/kubric>, clone the repo and put the UCR script under root folder before creating semi-realistic synthetic dataset.

```bash
git clone https://github.com/google-research/kubric.git
git clone https://github.com/DelinQu/Urban-Crossroads-Rolling-Shutter-Dataset.git
mv Urban-Crossroads-Rolling-Shutter-Dataset/* kubric/
sh main.sh
```

## Download

The dataset can be download from [here]

(https://drive.google.com/drive/folders/1wkFJDsLUgnZfRel0c_TsSyis_moZPk29?usp=sharing).

