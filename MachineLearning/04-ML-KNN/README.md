*最邻近规则分类*

#### 1 K-Nearest Neighbor算法
> 1968年提出了最初的临近算法，分类算法。输入基于实例的学习(instance-based learning), 懒惰学习(lazy learning).

#### 2 K-NN算法步骤
>1.以所有已知类别的实例作为参照，判断未知实例的类别。<br>
>2. 选择参数K<br>
>3. 计算未知实例与已知实例的距离<br>
>4. 选择最近的K个已知实例<br>
>5. 根据少数服从多数的投票法则(majority-voting)，让未知实例归类为K个最邻近样本中最多数的类别

#### 3 关于距离K的衡量方法
  **Eudidean Distance定义**
  
#### 4 改进版本
* 考虑距离，根据距离加上权重。比如：1/d(d:Distance)
