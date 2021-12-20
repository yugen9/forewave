### 1.1.4 队列(Queue)

队列(queue)是只允许在一端进行插入操作，而在另一端进行删除操作的线性表。

队列是一种特殊的线性表，它只允许在表的前端(front)进行删除操作，而在表的后端(rear)进行插入操作，和栈一样，队列是一种操作受限制的线性表。进行插入操作的端称为队尾，进行删除操作的端称为队头。

队列(queue)也是表，使用队列时插入和删除在不同的端进行。队列的基本操作是Enqueue(入队)，在表的末端(rear)插入一个元素，还有出列(Dequeue)，删除表开头的元素。

代码实现：

```python
class Queue(object):
    def __init__(self):
        self.queue=[]
    def isEmpty(self):
        return self.queue==[]
    def enqueue(self,x):
        self.queue.append(x)
    def dequeue(self):
        if self.queue:
            a=self.queue[0]
            self.queue.remove(a)
            return a
        else:
            raise IndexError,'queue is empty'
    def size(self):
        return len(self.queue)
```

#### 队列类型
* FIFO：       先进先出
* LIFO：       后进先出(相当于栈)
* 双端队列：LIFO和FIFO的结合，就是可从队首和队尾添加和删除元素。
* 循环队列：队首和队尾相连(可以解决假溢出)

##### 队列Queue(import queue)

> Lib/queue.py：
>
> ```python
> class Queue:
>     # Override these methods to implement other queue organizations
>     # (e.g. stack or priority queue).
>     # These will only be called with appropriate locks held
> 
>     # Initialize the queue representation
>     def _init(self, maxsize):
>         self.queue = deque()
> 
> class LifoQueue(Queue):
>     def _init(self, maxsize):
>         self.queue = []
>         
> class PriorityQueue(Queue):
>     def _init(self, maxsize):
>         self.queue = []  
>     
>     def _put(self, item):
>         heappush(self.queue, item)
> 
>     def _get(self):
>         return heappop(self.queue)
> ```

队列类型：

* FIFO(queue.queue)、
* LIFO(queue.LifoQueue)、
* 优先级队列(queue.PriorityQueue)# 优先级队列越低越先出来(堆)

在Python里，queue.Queue主要是为了线程间通信，作为“队列”只是附带的功能。而collections.deque就是个容器，和dict，list类似。Queue相比deque有个坏处：**慢**不少。

Queue是很高级的同步设施，有例如get_nowait，join等同步用接口，该阻塞就阻塞，该返回就返回。而deque只是个容器。其实从类名也有所反映，Queue是大写的首字母；而deque是和list, dict等一样是小写的首字母。

如上代码所示，实际上，Queue的底层使用了deque。又如_init()上面的注释所说，支持替换底层容器，例如:

Last In First Out，使用list替换了原本的deque

PriorityQueue更高级，不但使用list替换了，还用heappush和heappop替换了普通的append和pop，用堆实现了PriorityQueue。

**FIFO：**

```python
q=queue.queue(maxsize=10)     # 创建一个队列长度为10的对象
q.put(x)                      # 队尾插入数据x
q.get()                       # 队首删除数据并返回该数据
q.qsize()                     # 返回队列的大小
q.empty()                     # 判断队列是否为空：若为空则返回True，反之则FALSE
q.full()                      # 判断是否为满：与maxsize相呼应
```
##### 双端队列Deque[(from collections import deque)](https://docs.python.org/3.11/library/collections.html#module-collections)

> collections模块由Cpython中C代码实现，Modules/_collectionsmodule.c，由Modules/Setup文件导入到makesetup中编译成库(哪个库，研究Cpython时再找)
>
> > Lib/collections/\____init__\__.py:
> >
> > ```python
> > try:
> >     from _collections import deque
> > ```

双端队列（deque，全名double-ended queue），是一种具有队列和栈的性质的数据结构。

双端队列中的元素可以从两端弹出，其限定插入和删除操作在表的两端进行。双端队列可以在队列任意一端入队和出队。
```python
q=deque(5)         # 新建一个一个大小为5的deque对象
q.appendleft(x)：  # 在列表左侧插入	    O(1)
q.popleft()：      # 弹出列表左侧的值   O(1)
extendleft：       # 在左侧扩展        O(k)
q.append(x)：      # 在列表右侧插入     O(1)
q.pop()：          # 弹出列表右侧的值   O(1)
extend：           # 在右侧扩展        O(k)
q.rotate(-n)：     # 将左端的n个元素移动到右端   O(k)
q.rotate(n)：      # 将右端的n个元素移动到左端
'''
q=deque('abcdef')
q.rotate(-2)
print(q)           # deque(['c','d','e','f','a','b'])
q.rotate(2)
print(q)           # deque(['e','f','a','b','c','d'])
'''
q.remove('c')：    # 删除一个指定元素    O(n)
q.clear()：        # 清空链表所有元素，使其长度为0
q.reverse()：      # 将队列反转
q.count(x)：       # 返回q中x的数量
len(q)：           # 返回q的长度
```
##### 循环队列LoopQueue
队尾出来进队首，双端队列的rotate可以实现循环队列。

```python
# 循环队列
class LoopQueue:

    def __init__(self, max_size):
        self._queue = [None] * max_size
        self._front = 0
        self._rear = 0
        self._max_size = max_size

    # 让队列支持遍历，支持for语句
    def __iter__(self):
        cursor = self._front
        while cursor != self._rear:
            yield self._queue[cursor]
            cursor = (cursor + 1) % self._max_size

    def is_empty(self):
        return self._front == self._rear

    def enqueue(self, data):
        if (self._rear + 1) % self._max_size == self._front:
            print("the queue is full")
        self._queue[self._rear] = data
        self._rear = (self._rear + 1) % self._max_size

    def dequeue(self):
        if self._front == self._rear:
            return "the current size of the queue is 0"
        rm_data = self._queue[self._front]
        self._queue[self._front] = None
        self._front = (self._front + 1) % self._max_size
        return rm_data

    def size(self):
        """返回当前队列的长度"""
        return (self._rear + self._max_size - self._front) % self._max_size
    
    # 取队首数据
    def get_front(self):
        if self._front == self._rear:
            return None
        return self._queue[self._front]
```

下面的例子是用queue中的FIFO实现一个功能，6个人传土豆，每数到7就淘汰手中有土豆的人，直到最后只剩一个人。
```python
#循环队列，num一定要比人数多
import queue
def hotpotato(namelist,num):
    que=queue.Queue(len(namelist))
    for name in namelist:
        que.put(name)
    while que.qsize()>1:
        for item in range(num):
            que.put(que.get())
        que.get()
    return que.get() namelist=['a','b','c','d','e','f']
print(hotpotato(namelist,7))
```

##### 优先队列PriorityQueue

优先队列和普通队列结构一样，数据从逻辑队尾进入队列，数据从逻辑队首移除。不同的是，从队首移除数据总会移除优先级最高的数据，而从队尾加入数据，也是根据某种顺序添加到队列中

1. 优先队列的数据结构是基于完全二叉树的特点：从任一叶子节点开始到根结点的一条路径是有序列表，如果是最大堆，则由叶子结点到根结点的路径上的所有结点数据呈现从小到大的变化，而最小堆则刚好相反。完全二叉堆（树）又是二叉树类型中的一种，所以要理解原理，需要理解树结构相关的知识
2. 二叉堆（不论是最小堆还是最大堆结构），一般都会提供如下几个接口，用来构建优先队列，二叉堆的数据插入，二叉堆的数据删除，二叉堆的根结点元素的值，以及将杂乱的序列（列表等数据结构）转化为堆结构。优先队列也是通过二叉堆内部的这几个接口达成目的

```python
import heapq

class PriorityQueue(object):
    def __init__(self):
        self._queue = []        #创建一个空列表用于存放队列
        self._index = 0        #保证同等优先级元素插入时的正确排序
    
    def push(self, item, priority):
        """队列每个数据项都由（priority, index, item)元组构成"""
        heapq.heappush(self._queue, (-priority, self._index, item)) 
        self._index += 1
        
    def pop(self):
        #  heappop() 函数总是返回”最小的”的元素
        return heapq.heappop(self._queue)[-1]    #返回拥有最高优先级的项

class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item: {!r}'.format(self.name)

if __name__ == '__main__':
    >>> q = PriorityQueue()
    >>> q.push(Item('foo'), 1)
    >>> q.push(Item('bar'), 5)
    >>> q.push(Item('spam'), 4)
    >>> q.push(Item('grok'), 1)
    >>> q.pop()
    Item('bar')
    >>> q.pop()
    Item('spam')
    >>> q.pop()
    Item('foo')
    >>> q.pop()
    Item('grok')
```

#### 应用

著名的 约瑟夫斯问题(Josephus Problem)是应用队列(确切地说，是循环队列)的典型案例。在 约瑟夫斯问题 中，参与者围成一个圆圈，从某个人(队首)开始报数，报数到n+1的人退出圆圈，然后从退出人的下一位重新开始报数；重复以上动作，直到只剩下一个人为止。

值得注意的是，Queue类只实现了简单队列，上述问题实际上需要用循环队列来解决。在报数过程中，通过“将(从队首)出队的人再入队(到队尾)”来模拟循环队列的行为。

代码实现：
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
def josephus(namelist, num):
  simqueue = Queue()
  for name in namelist:
    simqueue.enqueue(name)
  while simqueue.size() > 1:
    for i in xrange(num):
      simqueue.enqueue(simqueue.dequeue())
    simqueue.dequeue()
  return simqueue.dequeue()
if __name__ == '__main__':
  print(josephus(["Bill", "David", "Kent", "Jane", "Susan", "Brad"], 3))
```

**代码实现：**

---

│  q1_queue.py 队列
│  q2_deque.py 双端队列
│  q3_circular_queue.py 列表实现循环队列
│  q3_circular_queue_linked_list.py 链表实现循环队列
│  q4_double_ended_queue.py 双端队列
│  q5_linked_queue.py 链表实现队列
│  q5_queue_on_list.py 链表实现队列
│  q6_priority_queue_using_list.py 列表实现优先队列
│  \__init__.py
│  队列Queue.md 学习笔记

