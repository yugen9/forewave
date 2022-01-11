## 4.5.2 VIP歌曲爬取

​        冬夜微醺，忽有故人心上过，刚哥无心睡眠，想听歌。于是刚哥上网搜索python，学习了起来。

### 一、网易云

#### 1.请求分析

  如果想要下载一首歌，我们首先要获取到这首歌所对应的url。打开网易云，随机选择一首歌进行播放，打开Chrome的开发者工具，刷新看一下对应的请求，找到我们想要的歌曲文件的url。
                                        <img src="https://1001-1308754723.cos.ap-shanghai.myqcloud.com/20200914161215899.png" alt="在这里插入图片描述" width="50%" />

分析对应的url，获取数据的url 为`https://music.xxx.com/weapi/song/enhance/player/url/v1?csrf_token=`，请求方式为`POST`。POST提交了两个参数`params`和`encSecKey`，很明显这两个参数都经过了加密处理，而且经过不断提交刷新发现，这两个参数值会变，可以猜测到加密时应该是有随机操作，但其长度始终不变，即参数params的长度为152，参数encSecKey的长度为256。

​                                        <img src="https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220111204914206.png" alt="image-20220111204914206" width="50%" /> 

#### 2. 参数分析

通过`Ctrl + Shift + F`全局搜索参数`encSecKey`定位到了两个文件，然后在`core_7a734ef25ee51b62727eb55c7f6eb1e8.js`这个文件里通过`Ctrl + F`定位到了接口函数：

​                                          <img src="https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220111205303736.png" alt="image-20220111205303736" width="50%" />  

```js
var bVZ8R = window.asrsea(JSON.stringify(i0x), bqN0x(["流泪", "强"]), bqN0x(Wx5C.md), bqN0x(["爱心", "女孩", "惊恐", "大笑"]));
e0x.data = j0x.cs1x({
    params: bVZ8R.encText,
    encSecKey: bVZ8R.encSecKey
})
```

函数`window.asrsea()`应该就是加密函数，传入四个参数，将加密后的结果赋值给变量`bVZ8R`，返回的结果有两个属性，即`encText`和`encSecKey`，也就是我们想要的参数`params`和`encSecKey`。在这里设置一个断点，看一下这几个参数：

<img src="https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220111210301927.png" alt="image-20220111210301927" width="50%" />

通过最右边的变量查看区`Watch`可以看到变量`bVZ8R`的值就是我们需要的参数的值，这证实了函数`window.asrsea()`就是加密函数，然后我们在控制台`Console`打印一下这几个变量:

```js
>JSON.stringify(i0x)
<"{"csrf_token":""}"
>bqN0x(["流泪", "强"])
<"010001"
>bqN0x(Wx5C.md)
<"00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
>bqN0x(["爱心", "女孩", "惊恐", "大笑"])
<"0CoJUm6Qyw8W8jud"
```

即加密函数window.asrsea()所需的四个参数值已经确定，分别是字符串"`{"csrf_token":""}`、`"010001"`、`"00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"`、`"0CoJUm6Qyw8W8jud"`，第三个参数是十六进制的形式，通过几次刷新，这几个值不变。

#### 3.加密分析
搜索asrsea定位到了该函数的初始定义位置：

<img src="https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220111220956988.png" alt="image-20220111220956988" width="50%" />

函数`window.asrsea()`就是函数`d`，它就是我们要找的加密函数，它接收的`d、e、f、g`四个参数对应的就是`window.asrsea()`函数的四个参数，即

```js
d = "{\"csrf_token\":\"\"}"
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
```

摘取这部分加密函数分析一下：

函数`a`的作用是从字符串`"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"`中随机生成长度为`a`的字符串：

```js
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
```

函数`b`的作用是对数据`a`进行AES加密，模式为`CBC`，最后通过`toString()`方法将结果转成字符串：

```js
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
```

函数`c`的作用是对数据`a`进行RSA加密，返回的结果是十六进制形式的字符串：

```js
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
```

函数d的作用是对数据d进行加密，得到两个加密的结果encText和encSecKey，加密流程是通过函数a随机产生一个长度为16的字符串，然后通过函数b进行第一次AES加密，然后再通过函数b对第一次的加密结果进行一次AES加密，得到结果encText，即对应我们的params，最后通过函数c进行一次RSA加密，得到结果encSecKey。

```js
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
```

#### 4.模拟加密

> 这里使用一个非常强大的加密算法库-----[PyCryptodome](https://www.pycryptodome.org/en/latest/)，具体使用方法请参考[官方文档](https://www.pycryptodome.org/en/latest/)。

```python
class EncryptText:
    def __init__(self):
        self.character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.iv = '0102030405060708'
        self.public_key = '010001'
        self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b' \
                       '5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417' \
                       '629ec4ee341f56135fccf695280104e0312ecbda92557c93' \
                       '870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b' \
                       '424d813cfe4875d3e82047b97ddef52741d546b8e289dc69' \
                       '35b3ece0462db0a22b8e7'
        self.nonce = '0CoJUm6Qyw8W8jud'

    def create16RandomBytes(self):
        """
        # 产生16位随机字符, 对应函数a
        :return:
        """
        generate_string = random.sample(self.character, 16)
        generated_string = ''.join(generate_string)
        return generated_string

    def AESEncrypt(self, clear_text, key):
        """
        AES加密, 对应函数b
        :param clear_text: 需要加密的数据
        :return:
        """
        # 数据填充
        clear_text = pad(data_to_pad=clear_text.encode(), block_size=AES.block_size)
        key = key.encode()
        iv = self.iv.encode()
        aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
        cipher_text = aes.encrypt(plaintext=clear_text)
        # 字节串转为字符串
        cipher_texts = base64.b64encode(cipher_text).decode()
        return cipher_texts

    def RSAEncrypt(self, i, e, n):
        """
        RSA加密, 对应函数c
        :param i:
        :return:
        """
        # num = pow(x, y) % z
        # 加密C=M^e mod n
        num = pow(int(i[::-1].encode().hex(), 16), int(e, 16), int(n, 16))
        result = format(num, 'x')
        return result

    def resultEncrypt(self, input_text):
        """
        对应函数d
        :param input_text:
        :return:
        """
        i = self.create16RandomBytes()
        # i = "g7E16vXN1O2T3o7V"
        encText = self.AESEncrypt(input_text, self.nonce)
        encText = self.AESEncrypt(encText, i)
        # print(len(encText))
        # print(encText)
        # encSecKey = self.RSAEncrypt(i.encode())
        encSecKey = self.RSAEncrypt(i, self.public_key, self.modulus)
        # print(len(encSecKey))
        # print(encSecKey)
        from_data = {
            'params': encText,
            'encSecKey': encSecKey
        }
        return from_data
```

整个加密流程模拟完了，结果也是正确的，但是，这里还存在一个问题，我们模拟出来的encText，也就是参数params长度不够。这里可以确定的是加密算法是没有错误的，传入的参数中d、e、f、g后面三个值是固定的，所以问题就基本锁定了：参数d的值不对。
继续debug，发现函数d又接收到了新的参数d，它的值是这样的：

<img src="https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220111230438261.png" alt="image-20220111230438261" width="50%" />

将它进行两次AES加密后encText的数据长度达到了128，说明这个还不是正确的。继续debug，最终得到了参数d真正的值：d: `"{"ids":"[35440198]", "level":"standard", "encodeType":"aac", "csrf_token":""}"`， 最后看一下最终的结果：

<img src="https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220111230608776.png" alt="image-20220111230608776" width="50%" />

至此，所有参数都模拟生成。使用这些参数发起请求，便得到要下载的歌曲的地址。

上面是搜索下载单首歌曲的申请，如果搜索歌手的歌曲，在网易云搜索界面上键入歌手开始搜索，会看到POST提交了两个参数params和encSecKey，和我们获取歌曲url 时一样，但参数params的长度变为了280，参数encSecKey的长度依旧不变，为256。由此可以确定，又是参数d发生了变化。经过几次debug，最终确定了参数d的值：
d = `"{"hlpretag":"<span class=\"s-fc7\">","hlposttag":"</span>","s":"本兮","type":"1","offset":"0","total":"true","limit":"30","csrf_token":""}"`

<img src="https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220111231146888.png" alt="image-20220111231146888" width="50%" />

使用模拟加密获取到的两个参数再次发起请求，发现得到的结果是空的，然后改了一下，将字典转为`json`格式，AES二次加密后参数`params`长度变为了`300`，然而却得到了数据。和我们在开发者模式下看到的结果一样，里面包含歌曲名、歌曲的id以及歌手名等信息。

```python
        id_d = {
            "hlpretag": "<span class=\"s-fc7\">",
            "hlposttag": "</span>",
            "s": name,
            "type": "1",
            "offset": "0",
            "total": "true",
            "limit": "30",
            "csrf_token": ""
        }

        id_from_data = self.encrypt.resultEncrypt(str(id_d))
```

得到歌曲的id后，下载便和文中开始的过程一样了。至此，便完成了歌手、歌曲的搜索并可以按歌曲id下载。

### 二、酷狗

打开酷狗音乐，搜索歌手。F12查看：

<img src="https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220111235503868.png" alt="image-20220111235503868" width="50%" />

依旧是个GET请求，url 为`https://complexsearch.xxxxx.com/v2/search/song?callback=callback123&keyword=%E6%9C%AC%E5%85%AE&page=1&pagesize=30&bitrate=0&isfuzzy=0&tag=em&inputtype=0&platform=WebFilter&userid=-1&clientver=2000&iscorrection=1&privilege_filter=0&srcappid=2919&clienttime=1599910861467&mid=1599910861467&uuid=1599910861467&dfid=-&signature=51F1A4D0FBB3DE862AD5E87364E6756A`，先简单分析一下它的参数是什么意思，参数keyword就是我们在搜索那里输入的内容，参数page为页数，参数pagesize表示每页显示多少条信息。可以推测出参数signature应该是很重要的，而且经过刷新发现参数`signature`、`clienttime`、`mid`和`uuid`每次都会发生变化，且后面三个一直相同。估计参数可能被加密了，全局搜索参数signature，将其定位：

<img src="https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220111235712524.png" alt="image-20220111235712524" width="50%" />

果然，参数`signature`被MD5加密了，打上几个断点，然后debug看一下：

<img src="https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220111235752036.png" alt="image-20220111235752036" width="50%" />

参数是20个，但是只有参数`clienttime`、`mid`和`uuid`发生变化，而且它们还相同，找一下它们来自哪里，向上定位到了它们的位置：

<img src="https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220111235848849.png" alt="image-20220111235848849" width="50%" />

发现是个时间序列，由JavaScript中的`getTime()`方法生成的，它返回的是毫秒数，在Python中可以用`time`模块的`time()`方法代替。下面来模拟一下`MD5`加密，这里可以使用Python的标准库`hashlib`：

```python
    def MD5Encrypt(self, text):
        # 返回当前时间的时间戳(1970纪元后经过的浮点秒数)
        k = time.time()
        k = int(round(k * 1000))
        info = ["NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt", "bitrate=0", "callback=callback123",
                "clienttime={}".format(k), "clientver=2000", "dfid=-", "inputtype=0",
                "iscorrection=1", "isfuzzy=0", "keyword={}".format(text), "mid={}".format(k),
                "page=1", "pagesize=30", "platform=WebFilter", "privilege_filter=0",
                "srcappid=2919", "tag=em", "userid=-1", "uuid={}".format(k), "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"]
        # 创建md5对象
        new_md5 = md5()
        info = ''.join(info)
        # 更新哈希对象
        new_md5.update(info.encode(encoding='utf-8'))
        # 加密
        result = new_md5.hexdigest()
        return result.upper()
```

解决了参数，拼接请求url，即可得到下载地址。

### 三、酷我

经测试，请求头需要带上`Cookie、csrf、Host、Referer、User-Agent`，常规操作。经分析，搜索URL必须的参数`key`，表示输入的搜索关键字。

### 四、QQ

没有加密，同理可得。



至此，刚哥点燃一支烟，长吁一口气。

【[代码实现]()】



## 附界面显示：

<img src="https://1001-1308754723.cos.ap-shanghai.myqcloud.com/image-20220111195548041.png" alt="image-20220111195548041" width="50%" />

  

