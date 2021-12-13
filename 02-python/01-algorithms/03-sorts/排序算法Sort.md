### 1.2.2排序算法

常见排序算法可以分为两大类：

非线性时间比较类排序：通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlogn)，因此称为非线性时间比较类排序。
线性时间非比较类排序：不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时间下界，以线性时间运行，因此称为线性时间非比较类排序。

排序算法的分类还可以分为两种：

内排序和外排序。在排序过程中，全部记录存放在内存，则称为内排序；如果排序过程中需要使用外存，则称为外排序。下面讲的排序都是属于内排序。

内排序有可以分为以下几类：

1.  插入排序：直接插入排序、二分法插入排序、希尔排序。
2.  选择排序：直接选择排序、堆排序。
3.  交换排序：冒泡排序、快速排序。
4.  归并排序
5.  基数排序

相关概念：
稳定：如果a原本在b前面，而a=b，排序之后a仍然在b的前面。
不稳定：如果a原本在b的前面，而a=b，排序之后 a 可能会出现在 b 的后面。
时间复杂度：对排序数据的总的操作次数。反映当n变化时，操作次数呈现什么规律。
空间复杂度：是指算法在计算机内执行时所需存储空间的度量，它也是数据规模n的函数。

<img src="https://img2018.cnblogs.com/blog/1696039/201909/1696039-20190903203734714-743188197.png" alt="img" width="60%;" />

#### 10种经典排序算法:[^1]

1. [**冒泡排序**](#1. 冒泡排序)
2. [**选择排序**](#2. 选择排序)
3. [**快速排序**](#3. 快速排序)
4. [**归并排序**](#4. 归并排序)
5. [**堆排序**](#5. 堆排序)
6. [**插入排序**](#6. 插入排序)
7. [**希尔排序**](#7. 希尔排序)
8. [**计数排序**](#8. 计数排序)
9. [**桶排序**](#9. 桶排序)
10. [**基数排序**](#10. 基数排序)

#### 1. 冒泡排序

冒泡排序（Bubble Sort）是一种比较简单的排序算法，它重复地走访过要排序的元素，依次比较相邻两个元素，如果它们的顺序错误就把他们调换过来，直到没有元素再需要交换，排序完成。

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQXcJQOiblMUJXPayib9uD6c3fVFyC6ZEnhEkB5eM4uqt3CaHz4mCpYtIg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%;" />

> 注：上图中，数字表示的是数据序列原始的索引号。

##### 算法过程

- 比较相邻的元素，如果前一个比后一个大，就把它们两个对调位置。
- 对排序数组中每一对相邻元素做同样的工作，直到全部完成，此时最后的元素将会是本轮排序中最大的数。
- 对剩下的元素继续重复以上的步骤，直到没有任何一个元素需要比较。

冒泡排序每次找出一个最大的元素，因此需要遍历 n-1 次 （n为数据序列的长度）。

##### 算法特点

什么时候最快（Best Cases）：当输入的数据已经是正序时。

什么时候最慢（Worst Cases）：当输入的数据是反序时。

##### Python代码

```
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(1, n - i):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
    return lst
```

冒泡排序是一种简单的排序算法，它也是一种稳定排序算法。其实现原理是重复扫描待排序序列，并比较每一对相邻的元素，当该对元素顺序不正确时进行交换。一直重复这个过程，直到没有任何两个相邻元素可以交换，就表明完成了排序。

##### 算法分析

冒泡排序是一种简单直接暴力的排序算法，为什么说它暴力？因为每一轮比较可能多个元素移动位置，而元素位置的互换是需要消耗资源的，所以这是一种偏慢的排序算法，仅适用于对于含有较少元素的数列进行排序。

1. 稳定性：我们从代码中可以看出只有前一个元素大于后一个元素才可能交换位置，所以相同元素的相对顺序不可能改变，所以它是**稳定排序**
2. 比较性：因为排序时元素之间需要比较，所以是**比较排序**
3. 时间复杂度：因为它需要双层循环n*(n-1))，所以平均时间复杂度为O(n^2)
4. 空间复杂度：只需要常数个辅助单元，所以空间复杂度为O(1)，我们把空间复杂度为O(1)的排序成为原地排序（in-place）
5. 记忆方法：想象成气泡，一层一层的往上变大

#### 2. 选择排序

##### 选择排序原理

选择排序（Selection Sort）的原理，每一轮从待排序的记录中选出最小的元素，存放在序列的起始位置，然后再从剩余的未排序元素中寻找到最小元素，然后放到已排序的序列的末尾。以此类推，直到全部待排序的数据元素的个数为零。得到数值从小到达排序的数据序列。

也可以每一轮找出数值最大的元素，这样的话，排序完毕后的数组最终是从大到小排列。

选择排序每次选出最小（最大）的元素，因此需要遍历 n-1 次。

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQ3lF7B2tiacQaEymLibIr7CAOIFeicZTT2JCnAibe85Iicc3CsNia1OQuLn8Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

##### Python代码

```
def selection_sort(lst):
    for i in range(len(lst) - 1):  
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j  
        lst[i], lst[min_index] = lst[min_index], lst[i] 
    return lst
```

选择排序算法每次选出最小的元素，需要遍历 n-1 次。

##### 算法分析

选择排序和冒泡排序很类似，但是选择排序每轮比较只会有一次交换，而冒泡排序会有多次交换，交换次数比冒泡排序少，就减少cpu的消耗，所以在数据量小的时候可以用选择排序，实际适用的场合非常少。

1. 比较性：因为排序时元素之间需要比较，所以是**比较排序**
2. 稳定性：因为存在任意位置的两个元素交换，比如[5, 8, 5, 2]，第一个5会和2交换位置，所以改变了两个5原来的相对顺序，所以为**不稳定排序**。
3. 时间复杂度：我们看到选择排序同样是双层循环n*(n-1))，所以时间复杂度也为：O(n^2)
4. 空间复杂度：只需要常数个辅助单元，所以空间复杂度也为O(1)
5. 记忆方法：选择对象要先选最小的

#### 3. 快速排序

快速排序（Quick Sort），是在上世纪60年代，由美国人东尼·霍尔提出的一种排序方法。这种排序方式，在当时已经是非常快的一种排序了。因此在命名上，才将之称为“快速排序”。

##### 算法过程

1. 先从数据序列中取出一个数作为基准数（baseline，习惯取第一个数）。
2. 分区过程，将比基准数小的数全放到它的左边,大于或等于它的数全放到它的右边。
3. 再对左右区间递归(recursive)重复第二步，直到各区间只有一个数。

因为数据序列之间的顺序都是固定的。最后将这些子序列一次组合起来，整体的排序就完成了。

如下图，对于数据序列，先取第一个数据 `15`为基准数，将比 `15` 小的数放在左边，比 `15` 大（大于或等于）的数放在右边

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQr57xuzsqCbOjfaS9B5eTNdynVokrtiaMTU7tvKebHPlj1KDYsQ7Fyxg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

接下来，对于左边部分，重复上面的步骤，如下图，取左边序列的第一个数据 `11` 为基准数，将比 `11` 小的数放在左边，比 `11` 大（大于或等于）的数放在右边。

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQWv4VXHwdI9v50ibl7BN4P6JXkf9DHtA3U9vTlSyNXebXNN57NiaicUicLg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

继续递归重复上述过程，直到每个区间只有一个数。这样就会完成排序

##### Python代码

```
def quick_sort(lst):  
    n = len(lst)
    if n <= 1:
        return lst
    baseline = lst[0] 
    left = [lst[i] for i in range(1, len(lst)) if lst[i] < baseline] 
    right = [lst[i] for i in range(1, len(lst)) if lst[i] >= baseline]
    return quick_sort(left) + [baseline] + quick_sort(right)
```

快速排序算法(Quick Sort)，它是处理大数据最快的排序算法之一。 1. 先从数列中 取出一个数作为基准数（baseline，习惯取第一个数）。 2. 分区过程，将比基准数小的数全放到它的左边,大于或等于它的数全放到它的右边。 3. 再对左右区间递归(recursive)重复第二步，直到各区间只有一个数。

##### 算法分析 

1. 快速排序的时间性能取决于递归的深度。
2. 当pivot_key恰好处于记录关键码的中间值时，大小两区的划分比较均衡，接近一个平衡二叉树，此时的时间复杂度为O(nlog(n))。
3. 当原记录集合是一个正序或逆序的情况下，分区的结果就是一棵斜树，其深度为n-1，每一次执行大小分区，都要使用n-i次比较，其最终时间复杂度为O(n^2)。
4. 在一般情况下，通过[数学归纳法](https://www.zhihu.com/search?q=数学归纳法&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A26844138})可证明，快速排序的时间复杂度为O(nlog(n))。
5. 但是由于关键字的比较和交换是跳跃式的，因此，快速排序是一种不稳定排序。
6. 同时由于采用的递归技术，该算法需要一定的辅助空间，其空间复杂度为O(logn)。



#### 4. 归并排序

##### 算法思想

归并排序（Merge Sort）是建立在归并操作上的一种有效的排序算法。该算法是采用分治法的一个非常典型的应用，归并排序将两个已经有序的子序列合并成一个有序的序列。

##### 算法流程

主要两步(拆分，合并)

- 步骤１：进行序列拆分，一直拆分到只有一个元素；
- 步骤２：拆分完成后，开始递归合并。

思路：假设我们有一个没有排好序的序列，那么我们首先使用拆分的方法将这个序列分割成一个个已经排好序的子序列（直到剩下一个元素）。然后再利用归并方法将一个个有序的子序列合并成排好序的序列。

##### 图解算法

###### 拆分

对于数据序列 `[15,11,13,18,10]` ,我们从首先从数据序列的中间位置开始拆分，中间位置的设置为

首次拆分如下：

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQxCb7dRYcyOAPIiahe3FfaXB77Cou7VGsibqSvmgr6xUoK9NWMrotvXTw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

第一次拆分后，依次对子序列进行拆分，拆分过程如下：

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQ5mfAeXlmqoAjYDE7C4yBknWRA76HE6vbBx08HkucwiaGfn3S7LaiaLGg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

###### 合并

合并过程中，对于左右分区以及其子区间，递归使用合并方法。先从左边最小的子区间开始，对于每个区间，依次将最小的数据放在最左边，然后对右边区间也执行同样的操作。

合并过程的完整图示如下：

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQsGsbXRcjyAPNZvT3UB7ZmXbI6do2ak1YibUlOFX3vd45pAjbuFDibzEQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

##### Python代码

```
def merge_sort(lst):
    def merge(left,right):
        i = 0
        j = 0   
        result = []    
        while i < len(left) and j < len(right):  
            if left[i] <= right[j]:    
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result = result + left[i:] + right[j:]
        return result
    n = len(lst)
    if n <= 1:     
        return lst 
    mid = n // 2 
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left,right)
```

归并排序算法(Merge Sort)，是建立在归并操作上的一种有效的排序算法。该算法过程主要分为拆分与合并两个步骤 步骤１：进行序列拆分，一直拆分到只有一个元素； 步骤２：拆分完成后，开始递归合并。

- 归并排序对原始序列元素分布情况不敏感，其时间复杂度为O(nlogn)。

- 归并排序在计算过程中需要使用一定的辅助空间，用于递归和存放结果，因此其空间复杂度为O(n+logn)。

- 归并排序中不存在跳跃，只有两两比较，因此是一种稳定排序。

总之，归并排序是一种比较占用内存，但效率高，并且稳定的算法。

##### 算法分析

1. 比较性：排序时元素之间需要比较，所以为**比较排序**
2. 稳定性：我们从代码中可以看到当左边的元素小于等于右边的元素就把左边的排前面，而原本左边的就是在前面，所以相同元素的相对顺序不变，故为**稳定排序**
3. 时间复杂度： 复杂度为O(nlogn)
4. 空间复杂度：在合并子列时需要申请临时空间，而且空间大小随数列的大小而变化，所以空间复杂度为O(n)
5. 记忆方法：所谓归并肯定是要先分解，再合并

 

#### 5. 堆排序

要理解堆排序（Heap Sort）算法，首先要知道什么是“堆”。

##### 堆的定义

对于 n 个元素的数据序列 ，当且仅当满足下列情形之一时，才称之为 `堆`:

**情形1：**

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQGI1Pr0OsnzEULdhECr9Hh3y0yIaybqm1S3CzuQia86cGyTqu8nv2icLw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

**情形2：**

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQCqaQPGiaqSHclI9Zt0EWlrtA1x99hr69vsOau01EBDwZxclCYb2VgFg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

若序列 是堆，则堆顶元素必为序列中n个元素的最小值或最大值。

`小顶堆`如下图所示：

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQtHDibayu7yJNmw4ALSsDqicHuMozYKqibx8bK4cMczI0rRohm02NWh3xA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

`大顶堆`如下图所示：

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQYYe8XpBLQp2BJNyaHp7J6gSibkY1f5Ub9FZZ8DSXkKLic5kNuDP3k4hw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

若在输出堆顶的最小值（或最大值）之后，使得剩余n-1个元素的序列重又建成一个堆，则得到n个元素的次小值（或次大值）。如此反复执行，便能得到一个有序序列，这个过程称之为 `堆排序`。

##### 堆的存储

一般用数组来表示堆，若根结点存在序号 `0` 处， `i` 结点的父结点下标就为 `(i-1)/2`。`i` 结点的左右子结点下标分别为 `2*i+1`和 `2*i+2` 。

对于上面提到的小顶堆和大顶堆，其数据存储情况如下：

小顶堆:

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQGLe04IvHoYURkHlcwfSBID1E4KA8TOibWUbj53FP3Psic3IsYWUdibG0Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

大顶堆:

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQFmr1hjZicFyvtd4TsjqW4509J54PwKJZYBfTZCq2BWo4icxHWtbXuFFw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

每幅图的右边为其数据存储结构，左边为其逻辑结构。

##### 堆排序

实现堆排序需要解决两个问题：

1. 如何由一个无序序列建成一个堆？
2. 如何在输出堆顶元素之后，调整剩余元素成为一个新的堆？

###### 堆的初始化

第一个问题实际上就是堆的初始化，下面来阐述下如何构造初始堆，假设初始的数据序列如下：

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQSyibVCK49VMicPmUAkvcSgA3PKXxlydb0UxlaJP7ficeXwpO9jPuuYickA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

咱们首先需要将其以树形结构来展示，如下：

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQNWmzjO3HM6Pfqp33rCOJTH0aSw71Pm71ic8arrVgebKe5WFJqEhTR3g/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

初始化堆的时候是对所有的非叶子结点进行筛选。

最后一个非终端元素的下标是 `[n/2]` 向下取整，所以筛选只需要从第 `[n/2]` 向下取整个元素开始，从后往前进行调整。

从最后一个非叶子结点开始，每次都是从父结点、左边子节点、右边子节点中进行比较交换，交换可能会引起子结点不满足堆的性质，所以每次交换之后需要重新对被交换的子结点进行调整。

以小顶堆为例，构造初始堆的过程如下：

<img src="https://mmbiz.qpic.cn/mmbiz_gif/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQlv5KOLspsBdqfAIvk9WUz4HpZMgI7QjKiaicib6EPok8LicPPVy86ArTug/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1" alt="图片" width="40%" />

###### 进行堆排序

有了初始堆之后就可以进行排序了。

堆排序是一种选择排序。建立的初始堆为初始的无序区。

排序开始，首先输出堆顶元素（因为它是最值），将堆顶元素和最后一个元素交换，这样，第n个位置（即最后一个位置）作为有序区，前n-1个位置仍是无序区，对无序区进行调整，得到堆之后，再交换堆顶和最后一个元素，这样有序区长度变为2。

大顶堆:

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQVSCEziccs87d2lFTaXoEupFZDoWpUZDpfwTwopCkwXvIRYcmpOFp1aA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

交换堆顶元素和最后的元素:

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQRxPpeY9MupfxDQP5aCS8oq02V6FmhyC0IfQsVnXPiaRaTh8L9m1MzNw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

无序区-1，有序区+1:

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQURaaIx2vibcz4n57mXIZOUnlqjibPDgicd6l6pygDf6lX8TvTIic4XDCIQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

不断进行此操作，将剩下的元素重新调整为堆，然后输出堆顶元素到有序区。每次交换都导致无序区-1，有序区+1。不断重复此过程直到有序区长度增长为n-1，排序完成。

对于堆初始化，以及堆排序，最好还是通过视频演示来理解，这样更直观。

堆排序算法(Heap Sort)，是一种常见的排序方法。 对于长度为n的数据序列，该算法过程主要分为几步： 1. 堆的初始化 2. 堆排序，无序区数列长度 -1，有序区数列长度 +1 。 3. 对无序区重复堆排序操作，直至有序区长度为n-1 

##### Python代码

```
def heap_sort(lst):
    def adjust_heap(lst, i, size):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        largest_index = i 
        if left_index < size and lst[left_index] > lst[largest_index]: 
            largest_index = left_index 
        if right_index < size and lst[right_index] > lst[largest_index]: 
            largest_index = right_index 
        if largest_index != i: 
            lst[largest_index], lst[i] = lst[i], lst[largest_index] 
            adjust_heap(lst, largest_index, size)

    def built_heap(lst, size):
        for i in range(len(lst)//2)[::-1]: 
            adjust_heap(lst, i, size) 

    size = len(lst)
    built_heap(lst, size) 
    for i in range(len(lst))[::-1]:         
        lst[0], lst[i] = lst[i], lst[0]
        adjust_heap(lst, 0, i) 
    return lst
```

堆排序的运行时间主要消耗在初始构建堆和重建堆的反复筛选上。
其初始构建堆时间复杂度为O(n)。
正式排序时，重建堆的时间复杂度为O(nlogn)。
所以堆排序的总体时间复杂度为O(nlogn)。

堆排序对原始记录的排序状态不敏感，因此它无论最好、最坏和平均时间复杂度都是O(nlogn)。在性能上要好于冒泡、简单选择和直接插入算法。

空间复杂度上，只需要一个用于交换的暂存单元。但是由于记录的比较和交换是跳跃式的，因此，堆排序也是一种不稳定的排序方法。

此外，由于初始构建堆的比较次数较多，堆排序不适合序列个数较少的排序工作。

#### 6. 插入排序

插入排序(Insertion Sort)就是每一步都将一个需要排序的数据按其大小插入到已经排序的数据序列中的适当位置，直到全部插入完毕。

插入排序如同打扑克牌一样，每次将后面的牌插到前面已经排好序的牌中。

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQvAaeibjWQAALwK9aLOUreBRzbrS9ialK5P8EpPWkAQsOlcFLLodctPkQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="20%" />

##### Python代码

```
def insertion_sort(lst):
    for i in range(len(lst) - 1):
        cur_num, pre_index = lst[i+1], i
        while pre_index >= 0 and cur_num < lst[pre_index]:
            lst[pre_index + 1] = lst[pre_index]
            pre_index -= 1
        lst[pre_index + 1] = cur_num 
    return lst
```

插入排序算法，就好像玩扑克牌一样，每次将待排序数据插入到已排序的数列中。

##### 算法分析

插入排序的适用场景：一个新元素需要插入到一组已经是有序的数组中，或者是一组基本有序的数组排序。 

1. 比较性：排序时元素之间需要比较，所以为**比较排序** 
2. 稳定性：从代码我们可以看出只有比较元素大于当前元素，比较元素才会往后移动，所以相同元素是不会改变相对顺序 
3. 时间复杂度：插入排序同样需要两次循坏一个一个比较，故时间复杂度也为O(n^2) 
4. 空间复杂度：只需要常数个辅助单元，所以空间复杂度也为O(1) 
5. 记忆方法：想象成在书架中插书：先找到相应位置，将后面的书往后推，再将书插入

#### 7. 希尔排序

##### 基本原理

希尔排序(Shell Sort)是插入排序的一种更高效率的实现。

希尔排序的核心在于间隔序列的设定。既可以提前设定好间隔序列，也可以动态的定义间隔序列。

这里以动态间隔序列为例来描述。初始间隔（gap值）为数据序列长度除以2取整，后续间隔以 前一个间隔数值除以2取整为循环，直到最后一个间隔值为 1 。

对于下面这个数据序列，初始间隔数值为5

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQXPWofbTwMHlddQ74s7k8uukd1c9iabibyXsHY8tmT0uTFBQB9CPR0ib4A/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

先将数据序列按间隔进行子序列分组，第一个子序列的索引为[0,5,10]，这里分成了5组。

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQHicoCicrjiagYWALDcb6o1picU2Txjc8py4Fp68iaIACfmMv4pEZDxdYh0A/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

为方便大家区分不同的子序列，对同一个子序列标注相同的颜色，分组情况如下：

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQTYF3yUy0qtI2szUT9ChnkyVicGhNuZFoKgAibyxARLAKIBxicbN3CxIPA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

分组结束后，子序列内部进行插入排序，gap为5的子序列内部排序后如下：

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQqBmAzuOG4VC9M9F7eLR1dqbjBeEv7uC9mI8Iw2FicvLhz1e0xAfcQKA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQuWWiaR0uBCtI3HY7Nhvf5wqWIdicBMiaJvZg9aWNg18lVkPnX88mV86eQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

> 注：红色箭头标注的地方，是子序列内部排序后的状态

接下来选取第二个间隔值，按照间隔值进行子序列分组，同样地，子序列内部分别进行插入排序；

如果数据序列比较长，则会选取第3个、第4个或者更多个间隔值，重复上述的步骤。

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQnxt7u8f6XBjD7YcAibLz1Sic48uTFRnHkqhoEx498s2vZSpxBURRpIjw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

gap为2的排序情况前后对照如下：

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQP4ibFMXQLEF3ib2Lslk6liawbKEDz8yicSUicHZGEqrVdpr4FVsPxt3OT4w/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

最后一个间隔值为1，这一次相当于简单的插入排序。但是经过前几次排序，序列已经基本有序，因此最后一次排序时间效率就提高了很多。

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQtzWINjbf00owIgExvGNQVlLfQdJ6m01p14Nibzgic8qRNBRMW9Pr5PkQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

##### Python代码

```
def shell_sort(lst):
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            for j in range(i, gap - 1, -gap):
                if lst[j] < lst[j - gap]:
                    lst[j], lst[j - gap] = lst[j - gap], lst[j]
                else:
                    break
        gap //= 2
    return lst
```

希尔排序是插入排序的一种更高效率的实现。

##### 算法分析

1. 比较性：排序时元素之间需要比较，所以为**比较排序**
2. 稳定性：因为希尔排序是间隔的插入，所以存在相同元素相对顺序被打乱，所以是不**稳定排序**
3. 时间复杂度： 最坏时间复杂度O(n^2) ；平均复杂度为：O(n^1.3)
4. 空间复杂度：只需要常数个辅助单元，所以空间复杂度也为O(1)
5. 记忆方法：插入排序是每轮都是一小步，希尔排序是先大步后小步，它第一个突破O(n2)的排序算法。

#### 8. 计数排序

##### 基本原理

计数排序（Counting Sort）的核心在于将输入的数据值转化为键，存储在额外开辟的数组空间中。计数排序要求输入的数据必须是有确定范围的整数。

算法的步骤如下：

先找出待排序的数组中最大和最小的元素，新开辟一个长度为 `最大值-最小值+1` 的数组；

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQZbRMWHsDphyfdEdbpjpribpz1wPTqvfIeQ2MQP8SbhEE993VSjJWyaA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

然后，统计原数组中每个元素出现的次数，存入到新开辟的数组中；

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQTibBstM799ep2orCCJTcHWsRnqnhKgJ40bdiavkvhLa3gYwTcFjicOOuw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

接下来，根据每个元素出现的次数，按照新开辟数组中从小到大的秩序，依次填充到原来待排序的数组中，完成排序。

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQmYWiaqyZQsOfYicAFiciaO2DF1tW1dtX5jCCOVJFI5za65iclp9DN0J5NPw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

##### Python代码

```
def counting_sort(lst):
    nums_min = min(lst)
    bucket = [0] * (max(lst) + 1 - nums_min)
    for num in lst:
        bucket[num - nums_min] += 1
    i = 0
    for j in range(len(bucket)):
        while bucket[j] > 0:
            lst[i] = j + nums_min
            bucket[j] -= 1
            i += 1
    return lst
```

计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中,计数排序要求输入的数据必须是有确定范围的整数。

#### 9. 桶排序

##### 基本思想

简单来说，桶排序（Bucket Sort）就是把数据分组，放在一个个的桶中，对每个桶里面的数据进行排序，然后将桶进行数据合并，完成桶排序。

该算法分为四步，包括划分桶、数据入桶、桶内排序、数据合并。

###### 桶的划分过程

这里详细介绍下桶的划分过程。

对于一个数值范围在10到 49范围内的数组，我们取桶的大小为10 （`defaultBucketSize = 10`），则第一个桶的范围为 10到20，第二个桶的数据范围是20到30，依次类推。最后，我们一共需要4个桶来放入数据。

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQoqrgmyR8nCj3BudibdpicBiareaqibyc7S5KyzibObRyY5Ub9eoqqkR84kg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQRbkiaMoBBTtnWqsSKCwdv1pT8unUmxCSTicQ7OR3KbsQDGTEMvRxpCOQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

##### 排序过程

对于下面这个数据序列，初始设定桶的大小为 20 （`defaultBucketSize = 20`），经计算，一共需要4个桶来放入数据。

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQ0Hyx7BgOD1AEIW4b80F1ER0SLEGwgyp0ERE8CSk4D744MdwsiadUMcQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

然后将原始数组按数值大小放入到对应的桶中，完成数据分组。

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQRq3LXeBibcsITx7E21tzm6Xqyx1bLHDYxpOiaGpCOOR2DuAUMob8bHQA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

对于桶内的数据序列，这时可以用冒泡排序、选择排序等多种排序算法来对数据进行排序。这些算法，在之前的视频里已有介绍，大家可以去了解下。

这里，我选用 `冒泡排序` 来对桶内数据进行排序。

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQB7VQAtfMF24VQuvAdYJmicjTbhy4QDeWv7ozT8yibXpB9Vz0zibQje9GA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

桶内排序完成后，将数据按桶的顺序进行合并，这样就得到所有数值排好序的数据序列了

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQr8vKfZSZQ8iaDfmhkIMrttvKBcehmcTjXB7ySyGpOCnr63Piasd6aRGg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

桶排序：简单来说，桶排序就是把数据分组，放在一个个的桶中，对每个桶里面的数据进行排序，然后将桶进行数据合并，完成桶排序。

##### Python代码

```
def bucket_sort(lst, defaultBucketSize=4):
    maxVal, minVal = max(lst), min(lst)
    bucketSize = defaultBucketSize
    bucketCount = (maxVal - minVal) // bucketSize + 1  
    buckets = [[] for i in range(bucketCount)]
    for num in lst:
        buckets[(num - minVal) // bucketSize].append(num)
    lst.clear()  
    for bucket in buckets:
        bubble_sort(bucket)  
        lst.extend(bucket)
    return lst
```

#### 10. 基数排序

基数排序（radix sort）属于“分配式排序”（distribution sort），它是透过键值的部份信息，将要排序的元素分配至某些“桶”中，以达到排序的作用。

基数排序适用于所有元素均为正整数的数组。

##### 基本思想

排序过程分为“分配”和“收集”。

排序过程中，将元素分层为多个关键码进行排序（一般按照数值的个位、十位、百位、…… 进行区分），多关键码排序按照从最主位关键码到最次位关键码或从最次位到最主位关键码的顺序逐次排序。

基数排序的方式可以采用最低位优先LSD（Least sgnificant digital）法或最高位优先MSD（Most sgnificant digital）法，LSD的排序方式由键值的最右边开始，而MSD则相反，由键值的最左边开始。

LSD的基数排序适用于位数小的数列，如果位数多的话，使用MSD的效率会比较好，MSD的方式恰与LSD相反，是由高位数为基底开始进行分配，其他的演算方式则都相同。

##### 算法流程

这里以最低位优先LSD为例。

先根据个位数的数值，在扫描数值时将它们分配至编号0到9的桶中，然后将桶子中的数值串接起来。

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQhSDRib25gcvXRvXgLuNA4z5n9JI4jDKRwzUcCjydL83DDLlEZQPXiavQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQLmYokzTGYfK0zTyUXCJPI3X5aiaML1EM8SC4vDYM4IHG9F5hIQtlYLw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

将这些桶子中的数值重新串接起来，成为新的序列，接着再进行一次分配，这次是根据十位数来分配。

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQd3Wh6tGmIvN5sGwZGk3uibUEu8ricgqwD2OLFeQFk2dTDs4Kq6nXMYLw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/gY6csrBUrKiacJuyvZz8SBGhlYgibCaWjQzaQKzL6N1Qu89Qou7icxyZQpthMcgrANePd0RJNI8icB26k6ib2UuIT5A/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="图片" width="40%" />

如果排序的对象有三位数以上，则持续进行以上的动作直至最高位数为止。

基数排序属于“分配式排序”，它是透过键值的部份信息，将要排序的元素分配至某些“桶”中，以达到排序的作用。

##### Python代码

```
# LSD Radix Sort
def radix_sort(lst):
    mod = 10
    div = 1
    mostBit = len(str(max(lst))) 
    buckets = [[] for row in range(mod)] 
    while mostBit:
        for num in lst:  
            buckets[num // div % mod].append(num)
        i = 0  
        for bucket in buckets:  
            while bucket:
                lst[i] = bucket.pop(0)
                i += 1
        div *= 10
        mostBit -= 1
    return lst
```
#### 总结

​       没有十全十美的算法，有有点就会有缺点，即使是快速排序算法，也只是整体性能上的优越，也存在排序不稳定，需要大量辅助空间，不适于少量数据排序等缺点。[^3]

- 如果待排序列基本有序，请直接使用简单的算法，不要使用复杂的改进算法。

- 归并排序和快速排序虽然性能高，但是需要更多的辅助空间。其实就是用空间换时间。

- 待排序列的元素个数越少，就越适合用简单的排序方法；元素个数越多就越适合用改进的排序算法。

- 简单选择排序虽然在时间性能上不好，但它在空间利用上性能很高。特别适合，那些数据量不大，每条数据的信息量又比较多的一类元素的排序。

  ---


1. 十种排序算法在时间、空间复杂度，实现难度，稳定性等指标上存在较大差异，但并没有最好最坏之说，适合的才是最好的。[^2]

2. 三种O(n^2)平均时间复杂度的排序算法在空间复杂度、稳定性方面表现较好，甚至在特定情况下即便考虑时间复杂度也是最佳选择。

3. 堆排序初始建堆过程较复杂，仅建堆时间复杂度就达到O(nlogn)，但之后的排序开销稳定且较小，所以适合大量数据排序。

4. 希尔排序性能看似很好，但实际上他的整体性能受步长选取影响较大，插入排序本质也使他受数据影响较大。

5. 归并排序在平均和最坏情况下时间复杂度都表现良好O(nlogn)，但昂贵的空间开销大O(n)。

6. 快速排序大名鼎鼎，但最坏情况下时间复杂度直逼O(n^2)，远不如堆排序和归并排序。

7. 基于比较排序的算法（如前七种）时间复杂度O(nlogn)已是下限。

8. 三种线性时间复杂度排序算法虽然在速度上有决定性的优势，但也付出了沉重的空间代价，有时数据的特点让这种空间代价变得无法承受。所以他们的应用对数据本身有着特定的要求。

9. 关于稳定性，希尔排序、快速排序和堆排序这三种排序算法无法保障。三种算法因为划分（子序列、大小端、左右孩子）后各自处理无法保证等值数据的原次序。

<img src="https://img-blog.csdn.net/20180407235139160" alt="img" width="60%" />



#### Reference
---

[^1]:  公众号：Python数据之道  《用Python实现十大经典排序算法》
[^2]:  https://zhuanlan.zhihu.com/p/60396074  《Python实现十大常用排序算法》
[^3]: https://zhuanlan.zhihu.com/p/26844138  《基于python的七种经典排序算法》
