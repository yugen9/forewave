### 1.1.6 哈希

#### 散列表（Hash Table）

散列表：所有的元素之间没有任何关系。元素的存储位置，是利用元素的关键字通过某个函数直接计算出来的。这个一一对应的关系函数称为散列函数或Hash函数。
采用散列技术将记录存储在一块连续的存储空间中，称为散列表或哈希表（Hash Table）。关键字对应的存储位置，称为散列地址。

散列表是一种面向查找的存储结构。它最适合求解的问题是查找与给定值相等的记录。但是对于某个关键字能对应很多记录的情况就不适用，比如查找所有的“男”性。也不适合范围查找，比如查找年龄20~30之间的人。排序、最大、最小等也不合适。

因此，散列表通常用于关键字不重复的数据结构。比如python的字典数据类型。

设计出一个简单、均匀、存储利用率高的散列函数是散列技术中最关键的问题。
但是，一般散列函数都面临着冲突的问题。
冲突：两个不同的关键字，通过散列函数计算后结果却相同的现象。collision。

##### 散列函数的构造方法

好的散列函数：计算简单、散列地址分布均匀

1. 直接定址法
   例如取关键字的某个线性函数为散列函数：
   f(key) = a*key + b (a,b为常数）
2. 数字分析法
   抽取关键字里的数字，根据数字的特点进行地址分配
3. 平方取中法
   将关键字的数字求平方，再截取部分
4. 折叠法
   将关键字的数字分割后分别计算，再合并计算，一种玩弄数字的手段。
5. 除留余数法
   最为常见的方法之一。
   对于表长为m的数据集合，散列公式为：
   f(key) = key mod p (p<=m)
   mod：取模（求余数）
   该方法最关键的是p的选择，而且数据量较大的时候，冲突是必然的。一般会选择接近m的质数。
6. 随机数法
   选择一个随机数，取关键字的随机函数值为它的散列地址。
   f(key) = random(key)

总之，实际情况下根据不同的数据特性采用不同的散列方法，考虑下面一些主要问题：

- 计算散列地址所需的时间
- 关键字的长度
- 散列表的大小
- 关键字的分布情况
- 记录查找的频率

##### 处理散列冲突

- 开放定址法

就是一旦发生冲突，就去寻找下一个空的散列地址，只要散列表足够大，空的散列地址总能找到，并将记录存入。

公式是：

![img](http://www.uml.org.cn/python/images/20171218332.png)

这种简单的冲突解决办法被称为线性探测，无非就是自家的坑被占了，就逐个拜访后面的坑，有空的就进，也不管这个坑是不是后面有人预定了的。

线性探测带来的最大问题就是冲突的堆积，你把别人预定的坑占了，别人也就要像你一样去找坑。

改进的办法有二次方探测法和随机数探测法。

- 再散列函数法
  发生冲突时就换一个散列函数计算，总会有一个可以把冲突解决掉，它能够使得关键字不产生聚集，但相应地增加了计算的时间。
- 链接地址法
  碰到冲突时，不更换地址，而是将所有关键字为同义词的记录存储在一个链表里，在散列表中只存储同义词子表的头指针，如下图：

<img src="http://www.uml.org.cn/python/images/20171218333.png" alt="img" width="50%" />

这样的好处是，不怕冲突多；缺点是降低了散列结构的随机存储性能。本质是用单链表结构辅助散列结构的不足。

- 公共溢出区法
  其实就是为所有的冲突，额外开辟一块存储空间。如果相对基本表而言，冲突的数据很少的时候，使用这种方法比较合适。

<img src="http://www.uml.org.cn/python/images/20171218334.png" alt="img" width="30%" />

* 双重散列法(Double Hashing)

> 双重哈希可以处理 :
> **(hash1(key) + i \* hash2(key)) % TABLE_SIZE**
> 这里 hash1() 、 hash2() 是hash 函数， TABLE_SIZE 是hash表大小
> (如果发生冲突，i递增然后重复运算)

通俗的二次Hash函数：**hash2(key) = PRIME – (key % PRIME)**
**PRIME**一般选择小于 **TABLE_SIZE** 的质数

该方法使用了两个散列函数h(key)和h1(key)，故也称为双散列函数探查法。

##### 散列表查找实现

下面是一段简单的实现代码：

```python
# 忽略了对数据类型，元素溢出等问题的判断。
 
class HashTable:
  def __init__(self, size):
    self.elem = [None for i in range(size)] # 使用list数据结构作为哈希表元素保存方法
    self.count = size # 最大表长
 
  def hash(self, key):
    return key % self.count # 散列函数采用除留余数法
 
  def insert_hash(self, key):
    """插入关键字到哈希表内"""
    address = self.hash(key) # 求散列地址
    while self.elem[address]: # 当前位置已经有数据了，发生冲突。
      address = (address+1) % self.count # 线性探测下一地址是否可用
    self.elem[address] = key # 没有冲突则直接保存。
 
  def search_hash(self, key):
    """查找关键字，返回布尔值"""
    star = address = self.hash(key)
    while self.elem[address] != key:
      address = (address + 1) % self.count
      if not self.elem[address] or address == star: # 说明没找到或者循环到了开始的位置
        return False
    return True
 
 
if __name__ == '__main__':
  list_a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
  hash_table = HashTable(12)
  for i in list_a:
    hash_table.insert_hash(i)
 
  for i in hash_table.elem:
    if i:
      print((i, hash_table.elem.index(i)), end=" ")
  print("\n")
 
  print(hash_table.search_hash(15))
  print(hash_table.search_hash(33))
```

##### 散列表查找性能分析

如果没发生冲突，则其查找时间复杂度为O(1)，属于最极端的好了。

但是，现实中冲突可不可避免的，下面三个方面对查找性能影响较大：

- 散列函数是否均匀
- 处理冲突的办法
- 散列表的装填因子（表内数据装满的程度）

**代码实现：**

│  h1_hash_table.py 哈希表
│  h2_hash_table_with_linked_list.py 分离链表哈希表
│  h3_quadratic_probing.py 二次探测哈希表
│  h4_double_hash.py 双重哈希表
│  prime_numbers.py 素数
│  \_\_init__.py
│  [哈希Hash.md](./哈希Hash.md)  学习笔记

