# OccNet

![OccNet Pipeline](../images/OccNet-pipeline.png)

## Two stages

* Reconstruction of Occupancy

    The goal of this stage is to obtain a representative occupancy descriptor for supporting downstream tasks

    First extracts multi-view feature $F_t$ from surrounding images, and feeds them into BEV encoder along with history BEV feature $B_{t−1}$ and current BEV query $Q_t$ to get current BEV feature

    Then, the image feature, the history and current BEV feature are together decoded into occupancy descriptor via Cascade Voxel Decoder

* Exploitation of Occupancy

    Downstream tasks based on the reconstructed occupancy descriptor

### Cascade Voxel Decoder

* **From BEV to Cascade Voxel**

    increase height, decrise feature dimension

* **Voxel-based Temporal Self-Attention**

    align the history $V'_{t-1,i}$ to the current occupancy features $V_{t,i}$ via the position of ego-vehicle

* **3D Deformable Attention**

    3D-DA in short, each voxel query only needs to interact with local voxels of interest ([Deformable DETR](https://arxiv.org/pdf/2010.04159.pdf))

    $$3D{-}DA(\boldsymbol{q},\boldsymbol{p},V'_{t,i})=\sum_{m=1}^MW_m\sum_{k=1}^KA_{mk}W'_kV'_{t,i}(\boldsymbol{p}+{\Delta}\boldsymbol{p}_{mk})$$

* **Voxel-based Spatial Cross-Attention**

    the voxel feature $V_{t,i}$ interacts with the multi-scale image features $F_t$ with 2D deformable attention

### Exploiting Occupancy on Various Tasks

* **Semantic Scene Completion**

    design the MLP head to predict the semantic label of each voxel, the flow head with $L_1$ loss are attached to estimate the flow velocity per occupied voxels

* **3D Object Detection**

    [BEVFormer](https://arxiv.org/pdf/2203.17270.pdf)

* **BEV segmentation**

    map representation and semantic segmentation are predicted from the BEV feature as in 3D object detection

    drivable-area head and the lane head for map representation, the vehicle segmentation head and the pedestrian segmentation head for semantic segmentation

* **Motion Planning**

    squeezed along the height dimension

## Benchmark

### OpenOcc

the authour generate occupancy data with dense and high quality occupancy annotations utilizing the sparse LiDAR information and 3D boxes, Moreover, they take the foreground object motion into consideration with additional flow annotation of object voxels

* Independent Accumulation of Background and foreground

* Generation of annotation

    first voxelize the 3D space and label the voxel based on the majority vote of labelled points in the voxel

    annotate the flow velocity of voxel based on the 3D box velocity

## Conclusion

The OccNet trained on semantic scene completion task can obtain general representation for 3D space owing to the scene reconstructed in the occupancy descriptor.
