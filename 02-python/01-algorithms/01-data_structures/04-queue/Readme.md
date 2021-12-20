## 队列Queue

**import queue**：

**from collections import deque：**

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

> collections模块由Cpython中C代码实现，Modules/_collectionsmodule.c，由Modules/Setup文件导入到makesetup中编译成库(哪个库，研究Cpython时再找)
>
> > Lib/collections/\____init__\__.py:
> >
> > ```python
> > try:
> >     from _collections import deque
> > ```

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



