# 现代投资组合理论与投资分析

## 风险条件下机会集的特征

$R_{ij}$ 是第 $i$ 种证券的第 $j$ 种收益可能，$p_{ij}$ 对应 $i$ 资产获得第 $j$ 种收益可能的概率，$M$ 是收益可能的种数，$n$ 是证券的种数。

### 确定平均收益

期望值（Expected Value）：$E(R_i) = \bar{R_i} = \sum_{j=1}^{M} \frac{R_{ij}}{M}$。

### 衡量离散程度

- **方差**（Variance）：
  - **极大似然估计**：$\sigma_i^2 = \frac{1}{M}\sum_{j=1}^{M} [p_{ij} (R_{ij} - \bar{R_i})^2]$。
  - 无偏估计：$\sigma_i^2 = \frac{1}{M-1}\sum_{j=1}^{M} [p_{ij} (R_{ij} - \bar{R_i})^2]$。
- **标准差**（Standard Deviation）是方差的平方根。
- 半方差（Semi-Variance）是低于平均收益的收益与平均收益的偏差值的平方的平均值。
- 下偏矩（Lower Partial Moment）。
- 在险价值衡量（Value at Risk Measure）：某个特定概率情况 p 下的最小期望损失。即投资者损失的金额超过该指标的概率不超过给定的概率，同时也是 p 分位数。

### 投资组合的方差

两种资产的取得各自最高和最低收益的条件相反（相关系数为 -1）时，总可以找到**某个**投资组合在所有市场条件下的收益保持一致（方差为 0）。如果一个资产的较好收益倾向于与另一种资产的较差收益同时发生，那么合理地选择两种资产的投资组合也会降低离散度。

当几种资产的收益彼此独立时，由这些资产构成的投资组合的离散程度（变异系数 $\delta$）会小于每一种资产的离散程度（变异系数 $\delta$）。

### 投资组合的一般特性

$R_{Pj}$ 代表投资组合的第 $j$ 种收益，$X_i$ 是投资第 $i$ 种资产的资金比重，$N$ 是资产种类总数。

$R_{Pj} = \sum_{i = 1}^{N} (X_i R_{ij})$。

$\bar{R_{P}} = \sum_{i = 1}^{N} (X_i \bar{R_i})$。

协方差（Covariance）：$\sigma_{ik} = \sum_{j = 1}^{M} \frac{(R_{ij} - \bar{R_i})(R_{kj} - \bar{R_k})}{M}$。

**相关系数**（Correlation Coefficient）：$\rho_{ik} = \frac{\sigma_{ik}}{\sigma_i \sigma_k}$。

$\sigma_{P}^2 = \sum_{i=1}^{N} (X_{i}^2 \sigma_{i}^2) + \sum_{i=1}^{N} \sum_{k=1, k \neq j}^{N} (X_{i} X_{k} \sigma_{ik})$。

特别地，若 $i = k$，则 $\sigma_{ik} = \sigma_i^2$。
$\sigma_{P}^2 = \sum_{i=1}^{N} \sum_{k=1}^{N} (X_{i} X_{k} \sigma_{ik})$。

若每种资产的投资比例均等，则 $\sigma_{P}^2 = \frac{1}{N} \bar{\sigma_j^2} + \frac{N - 1}{N} \bar{\sigma_{jk}} = \frac{1}{N}(\bar{\sigma_j^2} - \bar{\sigma_{jk}}) + \bar{\sigma_{jk}}$。

### 两个总结性的例子

#### 债券与股票的配置

#### 国内与国外市场的配置

## 描述有效投资组合

### 回顾两个风险资产的组合：不允许卖空的情形

投资组合由资产 A 和 B 组成。

$$\bar{R_P} = X_A \bar{R_A} + (1 - X_A) \bar{R_B} \tag{5-1}$$

$$\sigma_P^2 = X_A^2 \sigma_A^2 + (1 - X_A)^2 \sigma_B^2 + 2 X_A (1 - X_A) \rho_{AB} \sigma_A \sigma_B \tag{5-4*}$$

#### 情况 1:完全正相关（$\rho = +1$）

资产由大型汽车制造商 C（Colonel Motels）和某东部大城市的电力公司 S（Separated Edison）组成。

$\sigma_P = X_C \sigma_C + (1 - X_C) \sigma_S$

$\bar{R_P}^2 = X_C \bar{R_C} + (1 - X_C) \bar{R_S}$

则 $\bar{R_P}^2 = \frac{\sigma_P - \sigma_S}{\sigma_C - \sigma_S} \bar{R_C} + (1 - \frac{\sigma_P - \sigma_S}{\sigma_C - \sigma_S}) \bar{R_S} = \frac{\sigma_P - \sigma_S}{\sigma_C - \sigma_S} (\bar{R_C} - \bar{R_S}) + \bar{R_S}$。

#### 情况 2：完全负相关（$\rho = -1.0$）

$\sigma_P = \lvert X_C \sigma_C - (1 - X_C) \sigma_S \rvert$

#### 情况 3：资产收益之间不相关（$\rho = 0$）

由导数为 0，可得极小值点上（书上这个方程有点小问题）：

$$X_C = \frac{\sigma_S^2 - \sigma_C \sigma_S \rho_{CS}}{\sigma_C^2 + \sigma_S^2 - 2 \sigma_C \sigma_S \rho_{CS}} \tag{5-9*}$$

将 $\rho_{CS} = 0$ 代入可得

$$X_C = \frac{\sigma_S^2}{\sigma_C^2 + \sigma_S^2}$$

### 投资组合可能性曲线的形状

~~若以标准差为自变量、以期望收益为因变量，则曲线是向左（标准差更小的方向）凸的。~~（我觉得是这样的）

_可以看一下教材上的图留个印象，我就不瞎画了。_

#### 不允许卖空条件下的有效边界

有效边界（Efficient Frontier）：介于整体最小方差投资组合和最大收益组合之间的曲线。凹函数。~~向左凸~~

#### 允许卖空条件下的有效边界

卖空：在不拥有证券的情形下出售证券的过程。需要向证券经纪人借入证券，然后卖出。

通常需要向证券经纪人缴纳额外的保证金，且保证金不会产生利息，但分析中通常不考虑该部分。

在允许卖空交易的情况下，投资组合可以提供无限大的期望收益率。

这种情况下，有效边界仍然是凹的。~~向左凸~~

<!--这种情况下，有效边界是一条直线，称为**资本市场线**（Capital Market Line）。？Copilot 补全的-->

#### 无风险借贷条件下的有效边界

可以将无风险利率贷款视为一个有确定收益的资产。收益率记为 $R_F$，收益标准差为 0。

无风险资产和风险资产的组合的风险可表示为：

$$\sigma_C = X \sigma_A$$

则组合的期望收益可表示为：

$$\bar{R_C} = (1 - X) R_F + X \bar{R_A} = R_F + (\frac{\bar{R_A} - \sigma_F}{\sigma_A}) \sigma_C$$

在不知道任何投资者信息的条件下，确定最优风险投资组合的能力，被称为**分离定理**（Separation Theorem）。

注意以下三种情况：

- 投资者能按无风险利率放贷和借款。
- 投资者能按无风险利率放贷，而不能按无风险利率借款。
- 投资者能按无风险利率放贷，但必须按高于无风险利率的利率 $R_F^\prime$ 借款。

### 实例与应用

- 确定输入数据时的考虑

  1. 经通货膨胀调整优化的输入数据
  2. 输入数据估计值的不确定性

     收益预测分布（Predictive Distribution）的方差 $\sigma_{Pred}^2 = \sigma^2 + \frac{\sigma^2}{T}$

     相关系数对时间非常敏感。

  3. 短期输入数据和长期投资组合选择

     假定不同时间段的收益彼此不相关，则平均值的标准差随时间的平方根递减。

### 三个例子

## 计算有效边界的组合

### 允许卖空且允许无风险借贷

条件：

$$
\begin{cases}
\theta = \frac{\bar{R_P} - R_F}{\sigma_P} \\
\sum_{i=1}^{N} X_i = 1 \\
\end{cases}
$$

将 $\bar{R_P}$ 和 $\sigma_P$ 代入，得到：

$$
\theta = \frac{\bar{R_P} - R_F}{\sigma_P} = \frac{\sum_{i=1}^{N} X_i (\bar{R_i} - R_F)}{\sqrt{\sum_{i=1}^{N} X_i^2 \sigma_i^2 + \sum_{i=1}^{N} \sum_{j=1, i \neq i}^{N} X_i X_j \sigma_{ij}}}
$$

$$
\vec{\bar{R}} = \begin{bmatrix}
    \bar{R_1} \\ \bar{R_2} \\ \vdots \\ \bar{R_N}
\end{bmatrix},
\vec{Z} = \begin{bmatrix}
    Z_1 \\ Z_2 \\ \vdots \\ Z_N
\end{bmatrix},
\sigma^2 = \begin{bmatrix}
    \sigma_1^2  & \sigma_{12}  & \dots & \sigma_{1N}  \\
    \sigma_{12} & \sigma_{2}^2 & \dots & \sigma_{2N}  \\
    \vdots      & \vdots       &       & \vdots       \\
    \sigma_{1N} & \sigma_{2N}  & \dots & \sigma_{N}^2 \\
\end{bmatrix}
$$

则 $\lambda = \sum_{i=1}^{N} Z_i$，$\vec{\bar{R}} - R_F = \sigma^2 \vec{Z}$，$X_k = \frac{Z_k}{\sum_{i = 1}^{N} Z_i}$。

<!--则 $\theta = \frac{\vec{Z}^T (\vec{\bar{R}} - R_F)}{\sqrt{\vec{Z}^T \sigma^2 \vec{Z}}}$。Copilot补全的-->

有效集是一条直线，其截距为无风险利率，斜率等于超额收益率与标准差之比。

收益方差也可以通过 $\sigma_P^2 = \frac{\bar{R_P}-R_F}{\lambda}$ 计算。

### 允许卖空但不允许无风险借贷

### 不允许卖空但允许无风险借贷

$$
\begin{cases}
\theta = \frac{\bar{R_P} - R_F}{\sigma_P} \\
\sum_{i=1}^{N} X_i = 1 \\
\forall i, X_i \geq 0 \\
\end{cases}
$$

### 既不允许卖空也不允许无风险借贷

$$
\begin{cases}
\theta = \sum_{i=1}^{N} (X_i \sigma_i ^2) + \sum_{i=1}^{N} \sum_{j=1, j \neq i}^{N} (X_i X_j \sigma_{ij}) \\
\sum_{i=1}^{N} X_i = 1 \\
\sum_{i=1}^{N} (X_i \bar{R_i}) = \bar{R_P} \\
\forall i, X_i \geq 0 \\
\end{cases}
$$

### 纳入额外约束条件

最低股利收益率：

$$
\sum_{i=1}^{N} (X_i d_i) \geq D
$$

### 一个例子

三类美国资产：大盘股、小盘股和债券。
