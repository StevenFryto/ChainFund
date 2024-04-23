# ChainFund——基于区块链和推荐算法的智能众筹系统

## 算法设计

# 模型概览

此实现利用 PyTorch 创建了 `ContrastiveAndPredictiveModel`，包含多个组件：

- **BERT Tokenizer 和 Model**：预训练的文本嵌入组件。
- **MultiHeadAttention**：自定义的注意力机制。
- **对比和预测任务**：利用嵌入对用户行为和内容互动进行预测。

## MultiHeadAttention

`MultiHeadAttention` 类实现了一个缩放点积注意力机制，通过多个头并行处理，使模型能够同时关注来自不同表示子空间的信息。

### 公式
注意力函数可以描述为：

$$ \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V $$

其中：
- \( Q, K, V \) 分别为查询、键和值。
- \( d_k \) 为键的维度。

每一个都被分成多个“头”，允许模型在不同的表示空间中捕捉数据的不同方面。

## ContrastiveAndPredictiveModel

该模型组件使用嵌入和注意力来预测用户互动，并对正面和负面示例进行对比。

### 组件：
- **用户嵌入**：将用户 ID 嵌入到密集向量中。
- **发布者嵌入**：类似地嵌入发布者 ID。
- **BERT 模型**：为文本数据生成嵌入。
- **注意力层**：处理文本嵌入以有效整合上下文。
- **全连接层**：将注意力输出映射到预测任务空间（用户预测、互动时长）。

### 前向传播：
模型处理用户 ID、发布者 ID 和文本数据（正面和负面示例）的批次，计算嵌入和注意力驱动的特征，并预测结果，包括：
- 正面与负面内容互动（对比任务）。
- 互动时长。
- 基于内容预测用户。

## 损失函数

使用三个损失函数来训练此模型：

### 对比损失：
旨在区分正面和负面文本输入的输出嵌入。
$$ \text{contrastive\_loss} = \text{mean}\left(\text{max}(0, \text{margin} - (pos\_output - neg\_output))\right) $$

### 时长损失：
预测与实际互动时长之间的均方误差。
$$ \text{duration\_loss} = \text{MSE}(predicted\_duration, true\_duration) $$

### 用户预测损失：
对基于互动数据预测的用户进行交叉熵损失。
$$ \text{user\_prediction\_loss} = \text{CrossEntropy}(predicted\_user, true\_user) $$

## DynamicLossWeights

一个类，用于根据它们的性能动态调整每个损失函数的权重，以促进模型稳定性并专注于训练难度较高的方面。

### 更新机制：
每个损失的权重与它们最近的值成反比，归一化总和为一：
$$ \text{new\_weight} = \frac{1/\text{loss}}{\sum(1/\text{losses})} $$

这种机制有助于在训练过程中通过适应每个损失函数的相对难度来平衡学习不同任务。

## 训练循环

训练过程包括：
- 加载数据批次。
- 执行模型的前向传递。
- 计算每个损失及其加权总和。
- 进行反向传播并更新模型权重。
- 根据最新结果动态调整损失权重。

这种全面的方法允许模型有效地从复杂且多面向的数据（如用户与内容的互动）中学习。

