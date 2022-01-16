# Build-in

Python原生数据类型主要有Number、String、Byte、Boolean、None、List、Tuple、Set、Dict这九种，这篇文章主要讲一下字符串、列表、元祖、集合、字典这五种，剩下的四种大家可以自己了解一下。

## 字符串

![image-20220116110754065](https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220116110754065.png)

初始化一个字符串，方便后面在字符串上做一些操作。

```
In [5]: s1 = 'naitangmao'
In [6]: s1

Out[6]: 'naitangmao'
```

字符串的索引，需要注意的是索引下标从0开始。

```
In [9]: s1[2]
Out[9]: 'i'
```

字符串的切片，以冒号分隔首尾索引位置，是[start:end]结构，注意不包含end对应元素；冒号左边不写入索引表示从头开始，同理右边不写入索引表示截取到字符串末尾。

```
In [8]: s1[:3]#从0开始，0,1,2三个索引
Out[8]: 'nai'
```

还可以利用切片结合负索引实现翻转字符串。

```
In [35]: s1[::-1]
Out[35]: 'oamgnatian'
```

利用加法实现合并字符串。

```
In [49]: print('ab'+'%'+'cd')
ab%cd
```

查找，利用find方法查询元素时，会返回在字符串第一次出现的下标，未找到会返回-1。

```
In [11]: s1.find('a')
Out[11]: 1
```

替换，replace可以实现字符串中元素的替换，比如将'tang'替换成空格。

```
In [13]: s1.replace('tang',' ')
Out[13]: 'nai mao'
```

去空格，使用strip方法可以删除一个字符串首尾的空格，然后也支持指定要删除内容。

```
In [23]: s2 = '   aaabbbccc   '
In [24]: s2
Out[24]: '   aaabbbccc   '

In [25]: s2.strip()
Out[25]: 'aaabbbccc'

In [26]: s2 = s2.strip()
In [27]: s2.strip('a')#可以指定删除首尾的元素
Out[27]: 'bbbccc'
```

切割，split方法可以根据元素切割字符串，并存入列表；如果不输入参数，会直接将原字符串存入列表。

```
In [30]: s1 = 'naitangmao'
In [31]: s1.split('t')
Out[31]: ['nai', 'angmao']

In [32]: s1.split()
Out[32]: ['naitangmao']
```

判断一个元素是否存在于字符串中。

```
In [37]: 'nai' in s1
Out[37]: True
```

分隔，利用join方法可以将一个字符串作为分隔符，分隔另一个字符串。

```
In [38]: s1.join('!!!')
Out[38]: '!naitangmao!naitangmao!'
```

利用%向字符串中传入参数，%s传入字符串、%d传入整数、%f传入浮点数，且可以控制小数点后的位数。

```
In [40]: print('naitangmao是%s！' % '靓仔')
naitangmao是靓仔！
In [41]: print('naitangmao %d '% 66)
naitangmao 66
In [44]: print('naitangmao %.2f'% 3.1415)
naitangmao 3.14
```

也可以利用format向字符串中传入参数，且不需要在意参数类型。

```
In [46]: '{0}ai{1}ang{2}ao'.format('n','66','3.14')
Out[46]: 'nai66ang3.14ao'
```

利用反斜杠对字符串进行转义。

```
In [47]: print('\t')

In [48]: print('\\t')
\t
```

## 列表

![image-20211208193647512](C:\Users\yug\AppData\Roaming\Typora\typora-user-images\image-20211208193647512.png)

同样初始化一个列表，然后方便对列表做一系列操作。

```
In [52]: list1
Out[52]: [1, 3, 5, 7, 9, 11]
```

首先同样是列表的索引，列表也支持负索引。

```
In [53]: list1[2]
Out[53]: 5

In [55]: list1[-2]#负索引
Out[55]: 9
```

再拓展一下带有间隔的切片，字符串同样适用，就是在end之后再加上一个双引号，用来写入切片的间隔，这才是切片最完整的结构。

```
In [58]: list1[0:6:2]
Out[58]: [1, 5, 9]
```

利用index方法可以获取某个元素在列表中的位置索引，未找到的则会报错。

```
In [60]: list1.index(3)
Out[60]: 1
```

利用join方法将列表中的各个元素合并为字符串。

```
In [121]: list1 = ['a','b','c']
In [122]: ''.join(list1)
Out[122]: 'abc'
```

count方法可以统计一个元素在列表中出现的次数。

```
In [63]: list1.count(5)
Out[63]: 1
```

enumerate可以直接获取列表的索引和对应元素。

```
In [133]: index_ = []
In [134]: value_ = []
In [135]: for i,v in enumerate(list1):
     ...:     index_.append(i)
     ...:     value_.append(v)
     
In [136]: index_
Out[136]: [0, 1, 2, 3, 4]
In [137]: value_
Out[137]: [3, 1, 4, 2, 5]
```

利用zip方法合并两个列表。

```
In [139]: list3 = list(zip(index_,value_))
In [140]: list3
Out[140]: [(0, 3), (1, 1), (2, 4), (3, 2), (4, 5)]]
```

扩大列表的四种方法：

- 1、append：将一个元素添至列表尾部
- 2、insert：将一个元素插入至指定位置
- 3、extend：将一个列表的所有元素都添加至另一个列表中
- 4、+：将两个列表合并成一个新列表

```
In [68]: list1.append(12)
In [69]: list1
[1, 3, 5, 7, 9, 11, 12]

In [78]: list1.insert(0,0)
In [79]: list1
Out[79]: [0, 1, 3, 5, 7, 9, 11, 12]

In [80]: list1.extend([2,4])
In [81]: list1
Out[81]: [0, 1, 3, 5, 7, 9, 11, 12, 2, 4]

In [82]: list2 = [6,8]
In [83]: list3 = list1+list2
In [84]: list3
Out[84]: [0, 1, 3, 5, 7, 9, 11, 12, 2, 4, 6, 8]
```

删除列表元素的三种方法：

- 1、pop:从列表指定位置删除元素，并将其返回。如果没有指定索引，pop()返回最后一个元素，并从列表中删去。
- 2、remove：从列表中删去指定元素，没有则会报错。
- 3、del：也是利用索引删去列表中的某部分。

```
In [91]: list1.pop(3)
Out[91]: 7
In [92]: list1
Out[92]: [1, 3, 5, 9, 11]

In [94]: list1.remove(5)
In [95]: list1
Out[95]: [1, 3, 9, 11]

In [96]: del list1[1:3]
In [97]: list1
Out[97]: [1, 11]
```

翻转列表的三种方式：

- 1、reverse:就地倒排列表中的元素。
- 2、reversed:函数对列表进行反转，并返回一个新的迭代器，需要用list转换
- 3、切片结合负索引

```
In [99]: list1 = [1,3,5,7,9,11]
In [100]: print(list1.reverse())
[11, 9, 7, 5, 3, 1]

In [102]: list2 = list(reversed(list1))
In [103]: print(list2)
[11, 9, 7, 5, 3, 1]

In [105]: list1[::-1]
Out[105]: [11, 9, 7, 5, 3, 1]
```

实现列表排序的两种方式：

- 1、sort:对列表中的元素就地进行排序。
- 2、sorted:函数对列表进行排序，形成一个新列表
- 3、利用lambda自定义函数

这两种方法默认为升序，通过参数reverse可以更改排序方式。

```
In [106]: list2 = [3,5,2,7,1]
In [108]: list2.sort()
In [109]: list2
Out[109]: [1, 2, 3, 5, 7]

In [116]: list3 = sorted(list2,reverse = True)
In [117]: list3
Out[117]: [7, 5, 3, 2, 1]
#按照元祖中第二个元素的大小排序
In [141]: list4 = [(0, 3), (1, 1), (2, 4), (3, 2), (4, 5)]
In [142]: print(sorted(list4,key = lambda x: x[1]))
[(1, 1), (3, 2), (0, 3), (2, 4), (4, 5)]
```

sort和reverse这类就地处理列表的操作，针对可变的列表是可以的，但如果是不可变的元祖，只能用sorted和reversed这两种方式。

拷贝列表的三种方式：

- 1、利用切片直接赋值，浅拷贝
- 2、copy方法，浅拷贝
- 3、deepcopy方法，深拷贝

```
In [25]: list2 = list1[:]
In [26]: list3 = list1.copy()
In [27]: import copy
In [29]: list4 = copy.deepcopy(list1)
```

深拷贝和浅拷贝的区别因为涉及到数据结构，口头叙述不容易理解，网上有很多图例讲解的博客，大家可以了解一下。

## 元组

元组和列表是非常相似的，有一种类似近亲的关系，也就是说列表中很多操作同样适用于元组，比如索引、切片等等，但也有一部分不同，这里主要来说一下元组的特别之处。

首先元组又被称作带锁的列表，就是元组内的元素是不能随意更改的，比如你不能给元组中的一个元素随意赋值。

```
In [2]: tuple1 = (1,2,3)
In [3]: tuple1[2] = 4
#会发生报错，告诉你不支持这样的操作
TypeError: 'tuple' object does not support item assignment
```

元组的标志并不是单纯的小括号，而是逗号，或者小括号与逗号的结合，看下面这个例子。

```
In [31]: tuple2 = (1)
In [32]: type(tuple2)
Out[32]: int
In [33]: tuple3 = (1,)
In [34]: type(tuple3)
Out[34]: tuple
In [35]: tuple4 = 1,2,
In [36]: type(tuple4)
Out[36]: tuple
```

那如何初始化一个空元组呢？

```
In [39]: tuple5 = ()
In [40]: type(tuple5)
Out[40]: tuple
```

上面刚刚说过元组是不可变对象，自然也不会有append、insert、pop这类的操作。元组中增添可以利用"+"实现，删除则可以利用del，因为这是python自带的回收机制。

```
In [42]: tuple5 = tuple5[:] + (1,2,3,4,)
In [43]: tuple5
Out[47]: (1, 2, 3, 4)

In [50]: del tuple5 #不支持切片
In [51]: tuple5
NameError: name 'tuple5' is not defined
```

"*"在数值型之间为乘积运算符，而在列表和元组之间可以表示为重复运算符。

```
In [53]: tuple5 = (1,2)
In [54]: tuple5 * 3

Out[54]: (1, 2, 1, 2, 1, 2)
```

## 集合

![image-20220116110849324](https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220116110849324.png)

![image-20220116110946678](https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220116110946678.png)

集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。集合对象还支持联合、交、差和对称差集等数学运算。

首先可以利用大括号或set()函数创建集合，如果想要创建空集合，你必须使用set()而不是{}，{}用来创建字典。

```
In [57]: set1 = set()
In [58]: type(set1)
Out[58]: set
```

集合会本身会带有去重功能。

```
In [55]: set1 = {1,1,2,2,3,3,4}
In [56]: set1
Out[56]: {1, 2, 3, 4}
```

将集合转化为列表时，会自动排序。

```
In [74]: set2 = {5,5,4,2,2,0}
In [75]: list_ = list(set2)
In [76]: list_
Out[76]: [0, 2, 4, 5]
```

集合之间的一些运算操作。

```
In [60]: set1 = {1,2,3,4}
In [61]: set2 = {3,4,5}
#差
In [62]: set1 - set2
Out[62]: {1, 2}
#并
In [63]: set1 | set2
Out[63]: {1, 2, 3, 4, 5}
#交
In [64]: set1 & set2
Out[64]: {3, 4}
#只在set1或只在set2中
In [65]: set1 ^ set2
Out[65]: {1, 2, 5}
```

利用add向集合中增添元素,利用remove删除元素。

```
In [69]: set1 = {1,2,3}
In [70]: set1.add(5)
In [71]: set1
Out[71]: {1, 2, 3, 5}

In [72]: set1.remove(2)
In [73]: set1
Out[73]: {1, 3, 5}
```

## 字典

![image-20220116111035320](https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220116111035320.png)

![image-20220116111058123](https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220116111058123.png)

字典是Python中一个非常有用的原生数据类型，一般序列是用连续的整数作为索引，而字典是以关键字作为索引，且关键字要是任意不可变类型。理解字典时可以把它看做无序的键：值对(key:value对)集合，同一个字典中键必须互不相同，利用{}可以初始化一个空的字典。

```
In [77]: dict1 = {}
In [78]: type(dict1)
Out[78]: dict
```

如果确保一个键不在字典中，可以利用下面的方法向字典中添加元素。

```
In [81]: dict1 = {'a':1,'b':2}
In [82]: dict1['c'] = 3
In [83]: dict1
Out[83]: {'a': 1, 'b': 2, 'c': 3}
```

而如果这个键已经存在于字典中了，就表示为这个键赋值。

```
In [84]: dict1['b']=4
In [85]: dict1
Out[85]: {'a': 1, 'b': 4, 'c': 3}
```

keys()方法能够一次性获得字典中所有的键，values()方法则用来获取值，items()则是获取键值对的元组形式。

```
In [86]: list(dict1.keys())
Out[86]: ['a', 'b', 'c']

In [87]: list(dict1.values())
Out[87]: [1, 4, 3]

In [88]: list(dict1.items())
Out[88]: [('a', 1), ('b', 4), ('c', 3)]
```

元组形式或者列表中嵌套的元组的形式都可以转换成字典，因为要保持不可变性。

```
In [89]: dict2 = dict([('e',5),('f',6)])
In [90]: dict2
Out[90]: {'e': 5, 'f': 6}

In [91]: dict3  = dict((('g',7),('h',8)))
In [92]: dict3
Out[92]: {'g': 7, 'h': 8}
```

当然也可以通过'='赋值的形式创建一个字典。

```
In [93]: dict5 = dict(i = 8,j = 9)
In [94]: dict5
Out[94]: {'i': 8, 'j': 9}
```

查询一个键是否存在一个列表中。

```
In [96]: 'i' in dict5
Out[96]: True

In [97]: 'a' in dict5
Out[97]: False
```

根据键查询对应值的两种方式：

- 1、直接利用键的名字索引，不足的是如果字典中没有这个键则会发生报错。
- 2、利用get方法，可以设置不存在键名的情况下的返回值，默认返回None。

```
In [98]: dict5['i']
Out[98]: 8
In [99]: dict5['a']
KeyError: 'a'

In [101]: dict5.get('i')
Out[101]: 8
In [103]: dict5.get('a',"没有")
Out[103]: '没有'
```

字典中的几种删除方式：

- 1、pop()方法，与列表不同的是必须要传入一个字典中已有键的参数。
- 2、popitem()，类似于列表中的pop()，随机删除一组键值对而非删除最后一个，因为字典本身无序。
- 3、del方法，用于删除整个字典

```
In [107]: dict3
Out[107]: {'g': 7, 'h': 8}

In [109]: dict3.pop('g')
Out[109]: 7
In [110]: dict3.popitem()
Out[110]: ('h', 8)
```

clear()方法可以清楚字典中所有的键值对。

```
In [104]: dict5.clear()
In [105]: dict5
Out[105]: {}
```

setdefault()方法可以传入一组键值对，如果字典中已有同名键，则返回键在字典中对应的值，否则将传入的键值对存入字典中。

```
In [115]: dict2
Out[115]: {'e': 5, 'f': 6}

In [117]: dict2.setdefault('e',1)
Out[117]: 5

In [118]: dict2.setdefault('g',7)
Out[118]: 7
In [119]: dict2
Out[119]: {'e': 5, 'f': 6, 'g': 7}
```

update()方法可以用来更新字典：

- 如果字典中已有传入的键，则更新键对应的值。
- 如果没有，则将传入的键值对存入字典中。

```
In [121]: dict2.update({'g':10})
In [122]: dict2
Out[122]: {'e': 5, 'f': 6, 'g': 10}

In [123]: dict2.update(dict1)
In [124]: dict2
Out[124]: {'e': 5, 'f': 6, 'g': 10, 'a': 1, 'b': 4, 'c': 3}
```

