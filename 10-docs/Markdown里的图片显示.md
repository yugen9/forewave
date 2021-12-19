# Markdown里的图片显示

# 1. 单张居中显示：

```html
<div align=center>
    <img src="http://xxx.jpg" alt="链表" width="50%" height="50%" />
</div>

<center>
    <img src="http://dreamofbook.qiniudn.com/Zero.png">
</center>

<figure>
    <img src="http://xxx.jpg">
</figure> 
```

# 2. 固定图片宽度/高度：

```html
<img src="http://xxx.jpg" title="Logo" width="100" /> 
1
```

宽度是 Width，高度是 High。Title 为图片描述。

# 3. 两张并排显示：

```html
<figure class="half">
    <img src="http://xxx.jpg">
    <img src="http://yyy.jpg">
</figure>
1234
```

# 4. 三张并排显示：

```html
<figure class="third">
    <img src="http://xxx.jpg">
    <img src="http://yyy.jpg">
    <img src="http://zzz.jpg">
</figure>
12345
```

# 5. 固定宽度，并排显示并居中

就是把上面的几个例子合起来，下面给出代码

```html
<center class="half">
    <img src="http://xxx.jpg" width="300"/>
    <img src="http://yyy.jpg" width="300"/>
</center>
```