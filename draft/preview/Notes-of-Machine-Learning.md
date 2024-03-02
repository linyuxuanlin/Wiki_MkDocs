# Notes of Machine Learning

- 传统的编程：告诉计算机数据和计算规律，计算机输出结果。
- 机器学习的方法：告诉计算机数据和一部分答案（标签），计算机输出答案与规律。

机器学习的三种方法：监督学习（Supervised Learning）,无监督学习（Unsuoervised learing）和强化学习（RL, Reinforcement Learning）。

- **监督学习（Supervised Learning）**：通过已标注好的数据进行模型训练，从而利用训练好的模型来对新的数据进行预测。监督意味着已经有标注好的数据集。
- **无监督学习（Unsuoervised learing）**：无需标注数据（有时候人也不知道问题的准确答案），适用于聚类和降维。
  - 聚类（Clustering）：例如给出一堆图片，把相似的图片划分到一起。
  - 降维（Dimensionality Reduction）：数据特征过多、维度过高时，要将数据降到合适的低维空间处理，保留最重要的特征数据。主要算法有主成分分析（PCA, Principal Component Analysis）。
- **强化学习（Reinforcement Learning, RL）**：例如 Alpha Go 之类的应用。？

机器学习的流程：

【图】

---

区分运动鞋或高跟鞋，即使你脑子里没有一条明确的判别公式，但你也能够通过从小的不断重复训练，一看到就能判断鞋子的类型。

机器学习神经网络的方法也是一样，在大量的已知数据集中学习，让正确的神经元激活，建立连接。以后再输入新数据的时候，就能很容易地经过正确的神经元来解决问题。
