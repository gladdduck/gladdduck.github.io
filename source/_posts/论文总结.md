# Few-shot Object Detection


## 综述

#### Few-Shot Object Detection: A Comprehensive Survey
1. 问题定义:N-way K-shot表示使用K个样本来训练N个类别
2. 和few-shot learning,semi-supervised learning,increamental learning的区别
3. 使用到的技术:1)迁移学习2)度量学习3)元学习

**Dual-Branch meta learning:**
![](https://image.yayan.xyz/20231105141045.png)
实现思路:一个Query Branch用来提取待检测图像的特征,然后通过RPN和一个RoI Align得到Query Feature,再和Support Feature提取出来的Support特征(K shot,K>1取平均),进行Aggregation,然后送入RoI Head进行分类和回归.

1. 聚合相关改进
   1. Variant For Aggregation:
      - 缺点:在RPN之后进行聚合,需要RPN为新类别生成Proposal,但是RPN可能无法为新类别生成Proposal
       - 改进:在RPN之前进行聚合(AttentionRPN),然后将增强的特征送入RPN,生成Proposal
       - 改进:使用second-order pooling替换avg pooling,减少Support Feature的颜色,条纹,斑点带来的噪声
   2. Variant For Aggregation Operation
      - 缺点:简单的channel-wise 乘法不能充分利用Query和Support的特征
      - 改进:添加比例因子,使用卷积,利用更复杂的操作等
   3. Keep Spatial Information for Aggregation
      - 缺点:average pooling会丢失空间信息,convolution会导致空间信息不对齐
      - 改进:attention-based aggregation
   4. Attention-base Aggregation
       - Dual-Awareness Attention for Few-Shot Object Detection:增强前景,抑制背景并使用Query Feature Map促进空间位置的对齐
       - Object detection based on few-shot learning via instance-level feature correlation and aggregation:IFC module用于构造实例特征的相关性,ASA module增强查询和支持之间的特征灵敏度,减少冗余信息
       - Few-shot object detection with affinity relation reasoning:设计了一个亲和关系推理模块（ARRM）来促进支持特征和感兴趣区域特征的交互
       - One-Shot Object Detection with Co-Attention and Co-Excitation:使用非局部操作来探索每个查询-目标对中体现的共同注意,并且使用改进的SeNet分配候选区域的重要性
       - Adaptive Image Transformer for One-Shot Object Detection:将支持和查询作为Transformer的输入,来充分融合信息
   5. Multi-Level Aggregation
       - 缺点:只在特征抽取之后进行了一次聚合
       - 改进:使用PVTv2(Pyramid Vision Transformer)在特征抽取的时候进行多次融合
   6. Aggregation of Several Support Images
       - 缺点:多个Support Image的情况下,对特征图取平均,忽略了不同的信息
       - 改进:1)使用可学习的权重 2)使用softmax分配权重
  
2. Incorporate Relation between Caregories
    - 缺点:基本类别可以帮助识别新的稀疏类
    - 改进:1)融入语言特征 2)构建图关系(多类别关系增强特征,合并相似类别特征) 3)捕获类间相似性,增强泛化能力

3. Increase Discriminative power
    - 缺点:1)在聚合之后,通常使用交叉熵损失判别分类,更好的方法是使用度量学习 2)元学习学习去区分前景和背景,这导致有可能检测到不存在的物体
    - 改进:-1)GenDet和Meta DETR通过相似度矩阵最小化类间差异,最大化不同的支持向量 2)MM-FSOD使用皮尔斯系数聚合支持向量和查询向量 3)CME擦除最具辨别力的像素  -1)AttentionRPN使用多关系检测器来判断是否存有物体 2)对比学习测量用来区分不同的类别 3)GenDet使用额外的检测器检测基类,增强骨干网络提取更具代表性的特征

4. Improve representation capability
    - 缺点:base categories被视为负类,导致识别新类的表达能力不足
    - 改进:SPCN通过选择与基类不同的区域,并使用自监督的方式检测数据增强前后相同的非基类区域

5. Proposal-free Detector
   - 缺点:许多方法基于Faster RCNN,1)可能生成不准确的区域建议框,2)决定在区域建议框之前还是之后进行聚合
   - 改进:1)无提议框的模型更容易实现 2)基于YOLO 3)基于DETR

6. Keep the Performance on Base Categories
    - 缺点:学习新的类别之后,模型可能会导致灾难性遗忘
    - 改进:1)Meta Faster R-CNN使用一个额外的branch预测base categories,在训练期间固定 2)Sylph每个类别使用独立的分类器


7. Increase the Variance of Novel Categories
    - 缺点:直接应用数据增强效果不佳
    - 改进:TIP使用additional transformed guidance consistency loss,使得变化前后的图像特征保持一致

8. Incorporate Context Information
    - 缺点:在RoI pool或者RoI Align之后,可能导致丢失信息
    - 改进:DCNet使用三种不同分辨率执行并行池化


9.  Category-agnostic Bounding Box Regression


**Single-Branch meta learning:**

**Transfer Learning**


## 论文

**Few-Shot Object Detection with Attention-RPN and Multi-Relation Detector**




**Frustratingly Simple Few-Shot Object Detection**
![](https://image.yayan.xyz/20231112160553.png)

微调方法:
1. 使用Faster RCNN作为检测器,第一阶段正常训练
2. 在新类上微调时,只微调分类器,前面的固定,并且分类器改为cosine similarity classifier
$s_{i, j}=\frac{\alpha \mathcal{F}(x)_{i}^{\top} w_{j}}{\left\|\mathcal{F}(x)_{i}\right\|\left\|w_{j}\right\|}$
$s_{i,j}$代表了第$i$个区域建议框和第$j$个类别的相似度


**Few-shot Object Detection via Feature Reweighting(Meta-YOLO)**
![](https://image.yayan.xyz/20231112172223.png)
1. 一个元特征抽取模块(meta feature extractor:YOLOv2中的Darknet19),用来提取查询图像的元特征
2. 一个特征重加权模块(feature reweighting module),将支持图像抽取出全局特征(class-specific representation),用于调整元特征的贡献,获得(理解为抽取出支持图像的特征然后和查询图像的特征做一个channel-wise的乘法,来形成一个reweighting的特征(class-specific features)).
另一个理解:把支持图像的特征抽取成一个权重参数,用这个参数来动态调整查询图中的特征贡献,得到一个新的class-specific features

1. 将class-specific features送入YOLOv2的检测器中进行检测








































# Zero-shot Object Detection
## 综述

**A Survey of Vision-Language Pre-Trained Models**
视觉语言多模态综述
介绍了视觉语言多模态的1. 特征表示 2. 模态交互 3. 预训练任务 4. 下游任务 5. 方向
2022年之前的VL预训练模型和常用数据集

## 网页

**[Zero-Shot Object Detection介绍](https://www.width.ai/post/how-zero-shot-object-detection-changes-computer-vision-tasks-in-business)**

介绍了Zero-Shot Object Detection的基本概念，以及如何使用Region-CLIP进行Zero-Shot Object Detection

**[Zero-Shot Object Detection案例](https://www.pinecone.io/learn/series/image-search/zero-shot-object-detection-clip/)**

一个样例代码,使用CLIP进行检测

## 论文

**Zero-Shot Detection**
![](https://image.yayan.xyz/20231023204527.png)
![](https://image.yayan.xyz/20231031170459.png)

1. 利用BackBone抽出来图像的特征$T_F$
2. 在$T_F$上进行检测,得到目标的位置信息$T_L$
3. 在$T_F$上进行语义预测,得到目标的文本信息$T_S$
4. 把$T_F,T_L,T_S$拼接起来,进行置信度的预测,得到了最终的预测结果(x,y,w,h,cls)
5. 损失函数由1)位置损失 2)语义损失 3)置信度损失组成
6. 在验证过程中分为Test-Seen,Test-Unseen,Test-Mix三种情况


解决问题:
1. RPN可能无法提议出那么多没见过的物体
2. 基于YOLOv2,性能强大
3. 简单容易理解

**Zero-Shot Object Detection**

方法:

1. 两阶段检测器结构,对区域建议框内的物体抽取出图像特征
2. 通过映射将图像特征映射到文本特征空间(通过wordEmbedding得到)
3. 在公共空间计算图像特征和文本特征的相似度,得到未见物体的类别

解决问题:

1. 将未见物体分为背景的解决
    - 使用固定的背景类:在嵌入空间中为背景添加一个固定的向量
    - 将多个潜在的类分配给背景对象,不断的将背景框标记为对象反复训练
2. 密集采样嵌入空间:数据集中可见类太少了导致公共空间稀疏,未见类的语义和视觉之间无法对齐
   - 使用除了未见类之外的额外数据补充训练

**Region-CLIP**

1. 利用RPN从图像中提取出region,抽取出特征
2. 利用现有文本解析器,从文本中提取出concept,抽取出特征
3. 利用CLIP计算region和concept的相似度,得到region-text的配对
4. 利用三个损失函数训练模型










