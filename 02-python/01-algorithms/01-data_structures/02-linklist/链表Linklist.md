### 1.1.2 链表Linklist[^1]

链表是实现了数据之间保持逻辑顺序，但存储空间不必按顺序的方法。可以用一个图来表示这种链表的数据结构：

<center>
    <img src="https://zhaochj.github.io/images/2016-05-13-01.jpg" alt="链表" width="50%" height="50%" />
</center>

**基本要素：**

1. 结点(也可以叫节点或元素)，每一个结点有两个域，左边部份叫`值域`，用于存放用户数据；右边叫`指针域`，一般是存储着到下一个元素的指针
2. head结点，head是一个特殊的结节，head结点永远指向第一个结点
3. tail结点，tail结点也是一个特殊的结点，tail结点永远指向最后一个节点
4. None，链表中最后一个结点指针域的指针指向None值，因也叫`接地点`，所以有些资料上用电气上的接地符号代表None

**常用方法：**

1. LinkedList()           创建空链表，不需要参数，返回值是空链表
2. is_empty()             测试链表是否为空，不需要参数，返回值是布尔值
3. append(data)        在尾部增加一个元素作为列表最后一个。参数是要追加的元素，无返回值
4. iter()                       遍历链表，无参数，无返回值，此方法一般是一个生成器
5. insert(idx,value)   插入一个元素，参数为插入元素的索引和值
6. remove(idx)          移除1个元素，参数为要移除的元素或索引，并修改链表
7. size()                      返回链表的元素数，不需要参数，返回值是个整数
8. search(item)         查找链表某元素，参数为要查找的元素或索引，返回是布尔值

**链表种类：**单向链表、单向循环链表、双向链表、双向循环链表 

 <center>
     <img src="https://img-blog.csdn.net/20180721154905692?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNzcyODAzMQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="img"  width="50%" height="50%" />
 </center>             

#### 节点类

python用类来实现链表的数据结构，节点（Node）是实现链表的基本模块，每个节点至少包括两个重要部分。首先，包括节点自身的数据，称为“数据域”(也叫值域)。其次，每个节点包括下一个节点的“引用”(也叫指针)

实现一个Node类：

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

此节点类只有一个构建函数，接收一个数据参数，其中`next`表示指针域的指针，实例化后得到一个节点对象，如下：

```
node = Node(4)
```

此节点对象数据为`4`，指针指向None。

这样一个节点对象可以用一个图例来更形象的说明，如下：

<div align=center>
    <img src="https://zhaochj.github.io/images/2016-05-13-02.jpg" alt="链表"  width="40%" height="40%" />
</div>

#### 链表类

LinkedList类的构建函数：

```python
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
```

此类实例后会生成一个链表对象，初始化了`head`和`tail`节点，且两节点都指向`None`，实例化代码如下：

```python
link_list = LinkedList()
```

也可以用图形象的表示这个链表对象，如下：

<div align=center>
    <img src="https://zhaochj.github.io/images/2016-05-13-03.jpg" alt="链表"  width="40%" height="40%" />
</div>　　　　　　　　　　　　　

##### is_empty方法实现

is_empty方法检查链表是否是一个空链表，这个方法只需要检查`head`节点是否指向`None`即可，代码如下：

```python
def is_empty(self):
        return self.head is None
```

如果是空列表返回`True`，否则返回`False`

##### append方法实现

append方法表示增加元素到链表，这和insert方法不同，前者使新增加的元素成为链表中第一个节点，而后者是根据索引值来判断插入到链表的哪个位置。代码如下：

```python
def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
```

既然要新增加节点，首先把Node类实例化得到一个node对象。这里有两种情况需要考虑，一是链表是一个空链表时怎样append一个节点；二是当链表不是空链表时又怎样append一个节点？

当`if self.head is None:`为`True`时，把链表的`head`和`tail`都指向了`node`，假如我们执行了

```
link_list(append(4))
```

此时的链表结构如下图：

<img src="https://zhaochj.github.io/images/2016-05-13-04.jpg" alt="链表"  width="40%" height="40%" />

当`if self.head is None:`为`False`时,说明链表已经增加了一个节点了，再增加一个节点时`head`已经指向了第一个节点，所以不为`None`，比如增加的第二个节点为：

```
link_list(append(5))
```

增加第二个节点的操作需要分两步完成，第一步：`self.tail.next = node`，即把上一个节点的`next`指针指向当前`node`；第二步：`self.tail = node`，把`tail`移动到`node`，如下图：

<img src="https://zhaochj.github.io/images/2016-05-13-05.jpg" alt="链表"  width="50%" height="50%" />

移动完成后就成这样了：

<img src="https://zhaochj.github.io/images/2016-05-13-06.jpg" alt="链表"  width="50%" height="50%" />

当增加第三个、第四个等节点时，按照上边的操作依次类推。

##### iter方法实现

iter方法表示遍历链表。在遍历链表时也要首先考虑空链表的情况。遍历链表时从`head`开始，直到一个节点的`next`指向`None`结束，代码如下：

```python
def iter(self):
        if not self.head:
            return
        cur = self.head
        yield cur.data
        while cur.next:
            cur = cur.next
            yield cur.data
```

当是遍历一个空链表时，`if not self.head:`为`True`，直接返回`None`；如果不是空链表就让一个局部变量`cur`指向`head`,并把`head`的`data`属性`yield`出来，再对`cur`的`next`指针指向的对象做`while`循环，直到`next`指向`None`，这样就遍历了链表。

##### insert方法实现

假如采取`append`方法又增加了两个节点，增加完成后如下图：

<img src="https://zhaochj.github.io/images/2016-05-13-07.jpg" alt="链表"  width="50%" height="50%" />

如果想在数据域为`6`的那节点处插入一个节点，需要做的操作有两步：

1. 把新节点的next指针指向数据域为`6`的这个节点，即为数据域为`5`节点的next指向指向的对象
2. 把数据域为`5`节点的next指针指向新加的节点

注： 这两个步骤不能颠倒，如果颠倒，数据域为`6`的节点会被丢失，数据域为`7`的节点不再是链表的节点。

示意图如下：

<img src="https://zhaochj.github.io/images/2016-05-13-08.jpg" alt="链表"  width="50%" height="50%" />

还要额外考虑两种情况：

1. 空链表时
2. 插入位置超出链表节点的长度时
3. 插入位置是链表的最后一个节点时，需要移动tail

当是在链表最后一个节点插入时，示意图如下：

<img src="https://zhaochj.github.io/images/2016-05-13-09.jpg" alt="链表"  width="50%" height="50%" />

要在指定的索引位置插入一个节点，前提是需要找到这个位置，在链表中只有采用遍历的方式，具有O(n)的速度，最糟糕时会遍历链表的所有节点，而当找到插入点时，我们并不需要当前节点的信息，而是需要前一个节点的信息，所以代码中巧妙的使用了`while cur_idx < idx-1:`的方式，这样能使用`cur`这个变量能指向插入点上一个节点对象。

实现`insert`方法的代码如下：

```python
def insert(self, idx, value):
        cur = self.head
        cur_idx = 0
        if cur is None:
            raise Exception('The list is an empty list')
        while cur_idx < idx-1:
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_idx += 1
        node = Node(value)
        node.next = cur.next
        cur.next = node
        if node.next is None:
            self.tail = node
```

##### remove方法实现

remove方法接收一个idx参数，表示要删除节点的索引，此方法要考虑以下几种情况：

1. 空链表，直接抛出异常
2. 删除第一个节点时，移动head到删除节点的next指针指向的对象
3. 链表只有一个节点时，把head与tail都指向None即可
4. 删除最后一个节点时，需要移动tail到上一个节点
5. 遍历链表时要判断给定的索引是否大于链表的长度，如果大于则抛出异常信息

请看下边图例：

<img src="https://zhaochj.github.io/images/2016-05-13-10.jpg" alt="链表"  width="50%" height="50%" />

<img src="https://zhaochj.github.io/images/2016-05-13-11.jpg" alt="链表"  width="50%" height="50%" />

以下为remove函数的代码：

```python
def remove(self, idx):
       cur = self.head
       cur_idx = 0
       if self.head is None:  # 空链表时
           raise Exception('The list is an empty list')
       while cur_idx < idx-1:
           cur = cur.next
           if cur is None:
               raise Exception('list length less than index')
           cur_idx += 1
       if idx == 0:   # 当删除第一个节点时
           self.head = cur.next
           cur = cur.next
           return
       if self.head is self.tail:   # 当只有一个节点的链表时
           self.head = None
           self.tail = None
           return
       cur.next = cur.next.next
       if cur.next is None:  # 当删除的节点是链表最后一个节点时
           self.tail = cur
```

##### size函数实现

size函数不接收参数，返回链表中节点的个数，要获得链表的节点个数，必定会遍历链表，直到最后一个节点的`next`指针指向`None`时链表遍历完成，遍历时可以用一个累加器来计算节点的个数，如下代码：

```python
def size(self):
        current = self.head
        count = 0
        if current is None:
            return 'The list is an empty list'
        while current is not None:
            count += 1
            current = current.next
        return count
```

##### search函数实现

search函数接收一个item参数，表示查找节点中数据域的值。search函数遍历链表，每到一个节点把当前节点的`data`值与`item`作比较，最糟糕的情况下会全遍历链表。如果查找到有些数据则返回`True`，否则返回`False`，代码如下：

```python
def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found
```



#### Reference

---

[^1]: https://zhaochj.github.io/2016/05/12/2016-05-12-%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84-%E9%93%BE%E8%A1%A8/

