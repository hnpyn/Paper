# TPVFormer

![TPVFormer](../assets/images/TPVFormer.png)

## Hybrid explicit-implicit representations Approach

[Efficient Geometry-aware 3D Generative Adversarial Networks](https://arxiv.org/pdf/2112.07945.pdf)

### Generalizing BEV to TPV

![Voxel-BEV-TPV](../assets/images/Voxel-BEV-TPV.png)

three axis-aligned orthogonal TPV planes, may provide complementary clues

* **Point Querying formulation**

    A query point at (x, y, z) in the real world

![point-query](../assets/images/TPV-point-query.png)

* **Voxel feature formulation**

    the TPV planes, when expanded along respective orthogonal directions and summed up, construct a full-scale 3D feature space similar to the voxel feature space

### TPVFormer

* **Overall Structure**

![TPVFormer-pipeline](../assets/images/TPVFormer-pipeline_1.png)

* **TPVQueries**

    TPV query (learnable parameters and add 3D positional embedding) is a grid cell feature belonging to one of the three planes and used to encode view-specific information from the corresponding pillar region.

* **Image Cross-Attention (ICA)**

    for example TPV query located at $(h, w)$

    first calculate its coordinates $(x, y)$ in the top view in the real world

    second sample uniformly $N_{ref}^{HW}$ reference points for the query $\boldsymbol{t}_{h,w}$ along the orthogonal direction of the plane

    third project them into the pixel coordinate

    finally generate offsets and attention weights through two linear layers and updated TPV queries by summing up the sampled image features weighted by their attention weights

    ([Deformable convolution networks](https://arxiv.org/pdf/1703.06211.pdf)) ([Deformable DETR](https://arxiv.org/pdf/2010.04159.pdf))

* **Cross-View Hybrid-Attention (CVHA)**

    exchange their information across different views

    for example, for top planes, simply sample a few random points

    for the side and front planes, sample 3D points uniformly along the direction perpendicular to the top plane and project them onto the side and front planes

    calculate the sampling offsets and attention weights for each reference point through linear layers and sum up the sampled features weighted by their attention score

## Experiments

![TPVFormer-experiments](../assets/images/TPVFormer-experiments.jpeg)

![TPVFormer-experiments2](../assets/images/TPVFormer-experiments2.jpeg)

* 3D semantic occupancy prediction

    sparse supervision, dense prediction

* LiDAR segmentation

* Semantic Scene Completion

## Conclusion

TPVFormer is able to describe the finegrained structures of a 3D scene efficiently. It produces consistent semantic voxel occupancy prediction with only sparse point supervision during training
