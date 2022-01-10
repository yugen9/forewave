# 1.交换两个变量
a,b = b,a = 3,2
print(a,b)
# print(a+b)
# a = a ^ b		#a^b
# b = a ^ b		#(a^b)^b==a
# a = a ^ b		#(a^b)^a==b

# a = a + b
# b = a - b
# a = a - b

#2.反转列表
# print([1,2,3][::-1])
a = [1,2,3]
print(a[::-1] , len(a))
print(a[-3])
print(a[-1:-4:-1])

#6.生成逆序序列
list(range(10,-1,-1))

#3.合并两个字典
# print({**{'a':1,'b':2}, **{'a':5, 'c':3, 'e':7}})

x = {'a':1, 'b':2}
y = {'a':3, 'd':8, 'e':4}
z1 = {}
z1.update(x)
z1.update(y)

#print(y.update(x))

z2 = {**x, **y}
z3 = dict(x, **y)
print(z1, z2, z3)

#4.码列表去重
aa = [1,2,3,4,5,5,6,67,4,3,8]

print(dict.fromkeys(aa))
print(list(dict.fromkeys(aa)))
print(set(aa))

print(set([1,2,3]+[5,1]+[4]))

#5.多个列表中的最大值
print(max([ [1,2,3], [5,1], [4] ], key=lambda v: max(v)))
print(max(max([ [1,2,3], [5,1], [4] ], key=lambda v: max(v))))
print(max([ [1,2,3], [5,1], [4] ]))
print(max(max([ [1,2,3], [5,1], [4] ])))

#7.最长单词
str1 = 'Life is short , I use python'
print(max(str1.split(), key = len))

#8.最大值
lis = ['1', '100', '111', '2']
print(max(lis, key=lambda x:int(x)))
print(max(lis, key=int))

lii = [(1,'a'),(3,'v'),(-1,'w'),(9,"rrr")]
print(max(lii))
print(max(lii, key = lambda x:x[1]))

#9.乘法表
print ('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))

# for i in range(1,10):
#print([i for i in range(1,10)])

#10.多个变量赋值
a,b,c = 4,5.5,'Hello'
#print(a,b,c)
a,b,*c = [1,2,3,4,5]
print(a,b,c)

#11.列表中偶数的和
a = [1,2,3,4,5,6]
s = sum([num for num in a if num%2 == 0])
print(s)

#12.从列表中删除多个元素
a = [1,2,3,4,5]
del a[0::2]
print(a)

#13.读取文件
#lst = [line.strip() for line in open('data.txt')]
#print(lst)

# list(open('data.txt'))

# ##Using with will also close the file after use
# with open("data.txt") as f:
#     lst=[line.strip() for line in f]
#print(lst)

#14.将数据写入文件
with open("data.txt",'a',newline='\n') as f: 
    f.write("Python is awsome")

#15.创建列表
lst = list(range(0,10))
print(lst)

# lst = [i for i in range(0,10)]
# print(lst)

#16.映射列表或类型转换整个列表
list(map(int,['1','2','3']))

list(map(float,[1,2,3]))

[float(i) for i in [1,2,3]]

#17.创建集合
#### Square of all even numbers in an range
aa = {x**2 for x in range(10) if x%2==0}
print(aa)

#18.打印从1到20的数字。但如果是3的倍数，打印Fizz，如果是5的倍数，打印Buzz，
# 如果同时是3和5的倍数，打印FizzBuzz，否则打印数字。
print(['FizzBuzz' if i%3==0 and i%5==0
    else 'Fizz' if i%3==0 
    else 'Buzz' if i%5==0 
    else i  for i in range(1,20)])

#19.回文
text = 'level'
ispalindrome = text == text[::-1]
print(ispalindrome)

#20.用空格分隔的整数到一个列表
# lis = list(map(int, input().split()))
# print(lis)

#21.打印图案
n = 5
print('\n'.join('&' * i for i in range(1, n + 1)))

#22.查找阶乘
import math
n = 6
print(math.factorial(n))

from functools import reduce
print(reduce(lambda x,y:x*y, range(1,7)))

#23.斐波纳契数列
fibo = [0,1]
[fibo.append(fibo[-2]+fibo[-1]) for i in range(5)]
print(fibo)

#24. 质数
print(list(filter(lambda x:all(x % y != 0 for y in range(2, x)), range(2, 13))))

#25. 矩阵转置 
a=[[1,2,3],
   [4,5,6],
   [7,8,9]] 
transpose = [list(i) for i in zip(*a)]
print(transpose)

#26.计数
import re
print(len(re.findall('python','python is a programming language. python is python.')))

#27. 用其他文本替换文本
print("python is a programming language.python is python".replace("python",'Java'))

#28. 