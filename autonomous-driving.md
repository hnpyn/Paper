# Autonomous Driving

## Occupancy

### [CVPR 2023] TPVFormer: Tri-Perspective View for Vision-Based 3D Semantic Occupancy Prediction

Yuanhui Huang<sup>1,2*</sup>, Wenzhao Zheng<sup>1,2*</sup>, Yunpeng Zhang<sup>3</sup>, Jie Zhou<sup>1,2</sup>, Jiwen Lu<sup>1,2,†</sup>

( <sup>1</sup>Beijing National Research Center for Information Science and Technology, China <sup>2</sup>Department of Automation, Tsinghua University, China <sup>3</sup>PhiGent Robotics <sup>*</sup>Equal contribution <sup>†</sup>Corresponding author )

![TPVFormer Pipeline](./assets/images/TPVFormer-pipeline.png)

Vision-based, motivated by MonoScene, generalize BEV by accompanying it with two perpendicular planes to construct three cross-planes perpendicular to each other, can produces consistent semantic voxel occupancy prediction with only sparse point supervision during training. ([Details](./assets/TPVFormer.md))

[[Paper in arXiv](https://arxiv.org/pdf/2302.07817.pdf)] [[Code](https://github.com/wzzheng/TPVFormer)]

### [ICCV 2023] OccNet: Scene as Occupancy

Chonghao Sima<sup>1,3∗†</sup>, Wenwen Tong<sup>2∗</sup>, Tai Wang<sup>1,4</sup>, Li Chen<sup>1,3</sup>, Silei Wu<sup>2</sup>, Hanming Deng<sup>2</sup>, Yi Gu<sup>1</sup>, Lewei Lu<sup>2</sup>, Ping Luo<sup>3</sup>, Dahua Lin<sup>1,4</sup>, Hongyang Li<sup>1</sup>

( <sup>1</sup> Shanghai AI Laboratory <sup>2</sup> SenseTime Research <sup>3</sup> The University of Hong Kong <sup>4</sup> The Chinese University of Hong Kong <sup>∗</sup>Equal contribution <sup>†</sup>Project lead )

![OccNet Pipeline](./assets/images/OccNet-pipeline.png)

Vision-based, voxel-wise, two-stage framework, obtains robust occupancy features from images and supports multiple driving tasks. ([Details](./assets/OccNet.md))

[[Paper in arXiv](<https://arxiv.org/pdf/2306.02851.pdf>)] [[Code](<https://github.com/OpenDriveLab/OccNet>)]

## Semantic Segmentation

### [CVPR 2023] Temporal Consistent 3D LiDAR Representation Learning for Semantic Perception in Autonomous Driving

Lucas Nunes<sup>∗</sup>, Louis Wiesmann<sup>∗</sup>, Rodrigo Marcuzzi<sup>∗</sup>, Xieyuanli Chen<sup>∗</sup>, Jens Behley<sup>∗</sup>, Cyrill Stachniss<sup>∗,⋆,‡</sup>

( <sup>∗</sup>University of Bonn, <sup>⋆</sup>University of Oxford, <sup>‡</sup>Lamarr Institute )

![TARL Pipeline](./assets/images/TARL-pipeline.png)

A novel self-supervised pre-training for 3D LiDAR data able to learn a robust and temporally- consistent representation by clustering together points from the same object viewed at different points in time.

[[Paper in CVF](https://openaccess.thecvf.com/content/CVPR2023/papers/Nunes_Temporal_Consistent_3D_LiDAR_Representation_Learning_for_Semantic_Perception_in_CVPR_2023_paper.pdf)] [[Code](https://github.com/PRBonn/TARL)]
