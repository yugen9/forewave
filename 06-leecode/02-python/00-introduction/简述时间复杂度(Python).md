## 简述时间复杂度(Python)

### 时间复杂度：
​        时间复杂度通常用Big O notation来表示，常见的时间复杂度有：

* *O*(1)：           常数复杂度
* *O*(*log* *n*)：     对数复杂度
* *O*(*n*)：           线性时间复杂度
* *O*(*n* *^2^*)：         平方
* *O*(*n* *^3^*)：         立方
* *O*(*2* *^n^*)：         指数
* *O*(*n*!)：          阶乘

​       只看最高复杂度的运算，不考虑系数，比如线性时间复杂度*O* ( *n* ) ，并不意味着，程序执行了*n*次，也可能是2*n*次，但在描述时间复杂度时，通常忽略系数。
*O* (*1*) < *O* (*log* *n*) < *O* (*n*) < *O* (*nlog* *n*) < *O* (*n* *^2^*) < *O* (*n* *^2^* *log n*) < *O* (*n* *^3^*) 

1.  ***O*(*1*)** **：常数复杂度**

   ```python
   '''程序1：'''
   a = 500
   print("a 的值为：",a)
   '''程序2：'''
   b = 1000
   print(a)
   print(b)
   ```

   上面的两个程序分别执行了1次和2次，省略常数，他们的时间复杂度都记为*O*(*1*)。
   
2. ***O*(*log* *n*)：对数复杂度**

   ```python
   nums = [1,2,3,4]
   key = 5
   count = 0
   l, r = 0, len(nums)-1
   while l<r:
       mid = (l+r)//2
       if nums[mid] == key:
           count += 1
           break
       elif nums[mid] >key:
           count += 1
           r = mid-1
       else:
           count += 1
           l = mid +1
   print('程序共被执行了：',count,'次')
   ```

   对数时间复杂度最经典的例子是折半查找。但这半查找可能不是很直观，下面是一个非常简单的例子：

   ```python
   n = 64
   count = 0
   while n>1:
       n = n//2
       count += 1
   print('程序共被执行了：',count,'次')
   ```

   2^6^ = 64，log~2~64 = 6，所以循环减半的时间复杂度为*O*(*log*~2~n)，即*O*(*log* *n*)。

3. ***O*(*n*)：线性时间复杂度**

   ```python
   n = 5
   count= 0
   for i in range(n):
   	count+=1
   print('程序共被执行了：',count,'次')
   ```

   最经典的时间复杂度为*O*(*n*)的结构为一层for循环（还有二叉树的遍历前中后层序，图的遍历，BFS，DFS：每个结点访问且仅一次），可以看到，当n为5时，程序执行5次，当n为100时，程序执行100次，时间复杂度随着n的变化作线性变化。
   
4. ***O*(*n* *^2^*)：平方**

   最经典的时间复杂度为*O*(*n* *^2^*) 的结构为二层for循环。

   ```python
   '''程序2：'''
   n = 5
   count = 0
   for i in range(n):
       for j in range(i):
           count += 1
   print('程序共被执行了：',count,'次')
   ```

   ```python
   程序共被执行了： 10 次
   ```

​      上述程序2一共被执行了：(1+n−1)∗(n−1)/2 = (n^2^−n)/2, 忽略常数系数以及只看最高复杂度，即为*O*(*n*^2^) 。

5. ***O*(*n* *^3^*) ：立方**

   ```python
   n = 5
   count = 0
   for i in range(n):
       for j in range(n):
           for k in range(n):
               count += 1
   print('程序共被执行了：',count,'次')
   ```

   ```python
   程序共被执行了： 125 次
   ```

   最经典的时间复杂度为*O*(*n* *^3^*) 的结构为三层for循环。

6. ***O*(*2* *^n^*)：指数**

   求斐波拉契数列的第n项（递归）：

   ```python
   n = 6
   def fib(n):
       if n<2:return n
       return fib(n-1)+fib(n-2)
   print('斐波拉契',n,'为：',fib(n))
   ```

   ```
   >>> 斐波拉契 6 为： 8
   ```

   

