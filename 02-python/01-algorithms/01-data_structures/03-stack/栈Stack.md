### 1.1.3  栈Stack

栈（stack）又名堆栈，它是一种运算受限的线性表。其限制是仅允许在表的一端进行插入和删除运算。这一端被称为栈顶，相对地，把另一端称为栈底。向一个栈插入新元素又称作进栈、入栈或压栈，它是把新元素放到栈顶元素的上面，使之成为新的栈顶元素；从一个栈删除元素又称作出栈或退栈，它是把栈顶元素删除掉，使其相邻的元素成为新的栈顶元素。

栈又被称为LIFO(后入先出)表。

```python
Stack()   # 建立一个空的栈对象
push()    # 把一个元素添加到栈的最顶层
pop()     # 删除栈最顶层的元素，并返回这个元素
peek()    # 返回最顶层的元素，并不删除它
isEmpty() # 判断栈是否为空
size()    # 返回栈中元素的个数
```

#### 栈的实现

```python
class Stack(object):
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return self.stack==[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.isEmpty():
            raise IndexError,'pop from empty stack'
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
```

####  栈应用

**检查程序中成对的符号**

程序的语法错误经常是由缺少一个符号造成的。可用栈来检查符号是否成对。做一个空栈，如果字符是开放符号('({[')则将其push栈中。如果符号是个闭合符号(')]}'),则当栈空时报错，对应'()}'的错误。否则，将栈pop，如果弹出的符号不是对应的开放符号，则报错，对应'(}'的错误。文件末尾，如果栈为空，则报错，对应'({}'的错误。 

```python
def match(i,j):
    opens='([{'
    closes=')]}'
    return opens.index(i)==closes.index(j)
def syntaxChecker(string):
    stack=Stack()
    balanced=True
    for i in string:
        if i in '([{':
            stack.push(i)
        elif i in ')]}':
            if stack.isEmpty():
                balanced=False
                break
            else:
                j=stack.pop()
                if not match(j,i):
                    balanced=False
                    break
    if not stack.isEmpty():
        balanced=False
    return balanced
```

**进制转换**

十进制转换二进制：把十进制转成二进制一直分解至商数为0。从最底左边数字开始读，之后读右边的数字，从下读到上。

<img src="https://images0.cnblogs.com/blog/601033/201402/201059591583022.png" alt="img" style="zoom:67%;" />

```python
def decimal_to_bin(dec):
    stack=Stack()
    cur=dec
    while cur>0:
        a=cur%2
        cur=cur/2
        stack.push(a)
    binstr=''
    while not stack.isEmpty():
        binstr+=str(stack.pop())
    return binstr
```

**后缀记法**

后缀记法(postfix)，使用一个栈，见到一个数时入栈，遇到一个运算符时就作用于从栈弹出的两个元素，将结果弹入栈中。

(7+8)/(3+2)可以写作7 8 + 3 2 + /

来自《Problem Solving with Algorithms and Data Structures》的图片：

<img src="https://images0.cnblogs.com/blog/601033/201402/201111392494571.png" alt="img" style="zoom:67%;" />

 中缀到后缀的转换：当读到一个操作数的时候，放到输出中。读到操作符(+,-,*,/)时，如果栈为空，则压入栈中，否则弹出栈元素放到输出中直到发现优先级更低的元素为止。读到'(',压入栈中，读到')',弹出栈元素并发到输出中直到发现'('为止。在末尾，将栈元素弹出直到该栈变成空栈。

来自《Problem Solving with Algorithms and Data Structures》的图片：

<img src="https://images0.cnblogs.com/blog/601033/201402/221113035229421.png" alt="img" style="zoom:67%;" />

```python
def infixtoPostfix(infix):
    a={}
    a['*']=3
    a['/']=3
    a['+']=2
    a['-']=2
    a['(']=1
    stack=Stack()
    post=''
    for i in infix:
        if i not in a and i!=')':
            post+=i
        elif i=='(':
            stack.push(i)
        elif i==')':
            top=stack.pop()
            while top!='(':
                post+=top
                top=stack.pop()
        else:         
            while not stack.isEmpty() and a[i]<=a[stack.peek()]:
                post+=stack.pop()
            stack.push(i)
    while not stack.isEmpty():
        post+=stack.pop()
    return post
                    
def postfixExp(postfix):
    stack=Stack()
    postlist=postfix.split()
    for i in postlist:
        if i not in '+-*/':
            stack.push(i)
        else:
            a=stack.pop()
            b=stack.pop()
            result=math(i,b,a)
            stack.push(result)
    return stack.pop()
def math(x,y,z):
    if x=='+':
        return float(y)+float(z)
    if x=='-':
        return float(y)-float(z)
    if x=='*':
        return float(y)*float(z)
    if x=='/':
        return float(y)/float(z)
```

