## 【转】Python数据分析及可视化



### [1.超硬核的 Python 数据可视化教程](https://mp.weixin.qq.com/s/zOB8AR80AzJ4raQ1Urud1Q)

### [2. 40个Python可视化图表案例](https://mp.weixin.qq.com/s/6rJu4X0ZnLTHKDDu6MWrUA)

### [3. 一篇 Python 数据可视化 "保姆级" 攻略](https://mp.weixin.qq.com/s/xRWHQUQNLcp63OJaXQGhMw)

### [4. 21款酷炫的数据可视化工具](https://mp.weixin.qq.com/s/XurgXcGFesunp_fqITyVSw)

### [5. 数据分析常用的知识点大全](https://mp.weixin.qq.com/s/yT0F8h6XrXO2wYTJmwHbmg)

### [6. （Tableau）做图似文章般行云流水](https://blog.csdn.net/qq_39783601/article/details/106105606)



### 8个流行的 Python可视化工具包：

**Matplotlib、Seaborn 和 Pandas**

把这三个包放在一起有几个原因：首先 Seaborn 和 Pandas 是建立在 Matplotlib 之上的，当你在用 Seaborn 或 Pandas 中的 df.plot() 时，用的其实是别人用 Matplotlib 写的代码。因此，这些图在美化方面是相似的，自定义图时用的语法也都非常相似。

Matplotlib 是比较低级的库，但它所支持的自定义程度令人难以置信（所以不要简单地将其排除在演示所用的包之外！），但还有其它更适合做展示的工具。

Matplotlib 还可以选择样式（style selection），它模拟了像 ggplot2 和 xkcd 等很流行的美化工具。

Matplotlib 及其相关工具的效率很高，但就演示而言它们并不是最好的工具。

**ggplot(2)**

「Aaron，ggplot 是 R 中最常用的可视化包，但你不是要写 Python 的包吗？」。人们已经在 Python 中实现了 ggplot2，复制了这个包从美化到语法的一切内容。

Pandas Python 包最近弃用了一些方法，导致 Python 版本不兼容。

如果你一定要在 Python 中用 ggplot，那你就必须要安装 0.19.2 版的 Pandas，但我建议你最好不要为了使用较低级的绘图包而降低 Pandas 的版本。

ggplot2（也包括 Python 的 ggplot）举足轻重的原因是它们用「[图形语法](https://www.zhihu.com/search?q=图形语法&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A1233577441})」来构建图片。基本前提是你可以实例化图，然后分别添加不同的特征；也就是说，你可以分别对标题、[坐标轴](https://www.zhihu.com/search?q=坐标轴&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A1233577441})、数据点以及趋势线等进行美化。

**Bokeh**

Bokeh 很美。从概念上讲，Bokeh 类似于 ggplot，它们都是用图形语法来构建图片，但 Bokeh 具备可以做出专业图形和商业报表且便于使用的界面。

Bokeh 提供的所有便利都要在 matplotlib 中自定义，包括 x 轴标签的角度、背景线、y 轴刻度以及字体（大小、斜体、粗体）等。下图展示了一些随机趋势，其自定义程度更高：使用了图例和不同的颜色和线条。

Bokeh 还是制作交互式商业报表的绝佳工具。

**Plotly**

Plotly 非常强大，但用它设置和创建图形都要花费大量时间，而且都不直观。

Ploty 入门时有一些要注意的点：

- 安装时要有 API 秘钥，还要注册，不是只用 pip 安装就可以；
- Plotly 所绘制的数据和布局对象是独一无二的，但并不直观；

但它也有优点，而且设置中的所有缺点都有相应的解决方法：

- 你可以在 Plotly 网站和 Python 环境中编辑图片；
- 支持交互式图片和商业报表；
- Plotly 与 Mapbox 合作，可以自定义地图；
- 很有潜力绘制优秀图形。

**Pygal**

Pygal 的名气就不那么大了，和其它常用的绘图包一样，它也是用[图形框架](https://www.zhihu.com/search?q=图形框架&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A1233577441})语法来构建图像的。由于绘图目标比较简单，因此这是一个相对简单的绘图包。使用 Pygal 非常简单：

- 实例化图片；
- 用图片目标属性格式化；
- 用 figure.add() 将数据添加到图片中。

**Networkx**

虽然 Networkx 是基于 matplotlib 的，但它仍是图形分析和可视化的绝佳解决方案。图形和网络不是我的专业领域，但 Networkx 可以快速简便地用图形表示网络之间的连接。

有很多数据可视化的包，但没法说哪个是最好的。希望你可以了解到在不同的情境下，该如何使用不同的美化工具和代码。

### 可视化工具：

#### 1、Echart

一个纯Javascript的数据可视化库，百度的产品，常应用于软件产品开发或网页的统计图表模块。可在Web端高度定制可视化图表，图表种类多，动态可视化效，各类图表各类形式都完全开源免费。能处理大数据量和3D绘图也不逊色，据说结合百度地图的使用很出色。

![img](https://1001-1308754723.cos.ap-shanghai.myqcloud.com/v2-3f76d954c3c5c5765eca365595a80609_720w.jpg)

Echart还是多用于一些开发场景的，但它也衍生了一个0代码的图表生成器—“[百度图说](https://www.zhihu.com/search?q=百度图说&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A1233577441})”，我体验了下，操作基本上就是选择图标，把数据复制过去，然后生成图表，保存为图或者代码嵌入。

#### 2、FineReport 可视化报表类——适合报表开发、BI工程师

一个报表软件，企业级的应用。用于系统的开发业务报表，数据分析报表。也可集成在OA，ERP，CRM等应用系统内，做数据报表模块，也可以开发成财务分析系统，就看你如何驾驭数据了。

两大核心功能是填报和数据展示，但我觉得比较惊艳的一点是，它内置了大量的图表和可视化动效，可视化很丰富，完全没有印象中做报表那种古板的风格。多以它能做出格式各样的dashboard、甚至是可视化大屏，一点不虚。

#### 3、Tableau 商业智能分析——适合BI工程师、数据分析师

几乎是数据分析师人人会提的工具，内置常用的分析图表，和一些数据分析模型，可以快速的探索式数据分析，制作数据分析报告。

因为是商业智能，解决的问题更偏向商业分析，用 Tableau可以快速地做出动态交互图，并且图表和配色也非常拿得出手。

Tableau最近也正在学习，可以参考我博客有关Tableau中的图，着实好用就对了，喜欢的就是它作图美观方便拖拽即可

#### 4、FineBI

自助是BI工具，也是一款成熟的数据分析产品。内置丰富图表，不需要代码调用，可直接拖拽生成。可用于业务数据的快速分析，制作dashboard，也可构建可视化大屏。

有别于Tableau的是，它更倾向于企业应用，从内置的ETL功能以及数据处理方式上看出，侧重业务数据的快速分析以及可视化展现。可与大数据平台，各类多维数据库结合，所以在企业级BI应用上广泛，个人使用免费。

![img](https://pic2.zhimg.com/80/v2-63572df66343e78e2fd1114b5a929fed_1440w.jpg?source=1940ef5c)

#### 5、PowerBI

软继Excel之后推出的BI产品，可以和Excel无缝连接使用，创建个性化的数据看板。

![img](https://1001-1308754723.cos.ap-shanghai.myqcloud.com/v2-3fd3df87bc1489ef233f672d7b8c2728_1440w.jpg)

#### 数据地图类

很多工具都能实现数据地图，比如上面提到的Echarts、finereport、tableau等。

这里强烈安利的Power Map 2016，可以快速体验一把爽。

![img](https://1001-1308754723.cos.ap-shanghai.myqcloud.com/v2-c56511ef9ae85b0d30c9272b684e9eef_720w.jpg)

还有比较快速的，地图慧，内置的是百度地图，选择模板、上传数据、保存地图很简单的3步。

### 可视化大屏类

#### 6、阿里DataV

天猫双十一大屏就用DataV做的，是阿里云的拖拽式可视化工具，主要用于业务数据与地理信息融合的大数据可视化，像一些展览中心，企业管控中心用。

不需要编程，通过简单的拖拽配置就能生成可视化大屏或者仪表盘。

![img](https://1001-1308754723.cos.ap-shanghai.myqcloud.com/v2-6e4921ead943c0a0d5a55e6d4bf67839_1440w.jpg)

#### FineReport

上面提过，这个工具它也能做可视化报表，也能做大屏。

因为后端通常连接业务系统数据，所以可以实时连接业务数据，做企业的一些经营数据展示。比如展览中心、BOSS驾驶舱，还有城市交通管控中心、交易大厅等。

![img](https://1001-1308754723.cos.ap-shanghai.myqcloud.com/v2-a84902e39be083e9a3c32e3d44b7842f_1440w.jpg)

#### 7、R-ggplot2

![img](https://1001-1308754723.cos.ap-shanghai.myqcloud.com/v2-5f3072e5ae7f803c8788b12f12cc3d21_1440w.jpg)

![img](https://1001-1308754723.cos.ap-shanghai.myqcloud.com/v2-4e0f1975993370bc75d462b262f6bdb5_1440w.jpg)

![img](https://1001-1308754723.cos.ap-shanghai.myqcloud.com/v2-8f9a7c3d093560841798c8570e1dffd0_1440w.jpg)

