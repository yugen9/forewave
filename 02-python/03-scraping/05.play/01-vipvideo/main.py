## 冬夜，微醺，巍哥想看片：于是巍哥打开视频网站查找，Copy了网址
## 然后巍哥开始学习：人生苦短，我用python

import os
import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as msgbox
from tkinter import scrolledtext
from tkinter.filedialog import askdirectory

from weivideo import WeiVideo

# main : tkinter图形界面  1. 观看 2. 下载
# LableFrame + grid, 各组件place确定其位置
class Weige():
    def __init__(self):
        # 上帝
        self.n = '巍哥'
        
        self.video = tk.Tk()
        self.video.title('冬夜，微醺，'+self.n+'想看片：')
        
        # 选择 电影 电视剧等 LabelFrame 1
        self.vf1=tk.LabelFrame(self.video, width=390, height=40)
        self.vf1.grid(row=0,column=0,padx=5, pady=10)

        # 观影类别
        self.vsrc = ['电影', '电视剧', '欧冠']

        # 选电影时不需要显示剧集的TEXT等组件
        def vsrc_rbn_call():
            if self.vsrc_rbn.get() == 1:      # 电影
                self.textdestroy()            # 去掉显示剧集的TXT组件
                self.down_config('disabled')  # 禁用下载序号等组件
                self.line_var.set('Line-1')   # 线路1比较好没有广告
                self.now_line_number = 1      # 电影默认线路一
                self.v.switch_line(0)
    
            elif self.vsrc_rbn.get() == 2:    # 电视剧
                self.textcreate()
                self.down_config('normal')
                self.line_var.set('Line-2')   # 选电视剧用线路2可以显示剧集
                self.now_line_number = 2      # 电视剧默认线路二
                self.v.switch_line(1)

        self.vsrc_rbn = tk.IntVar()
        self.vsrc_rbn.set(1)
        for col in range(len(self.vsrc)):   # 创建单选按钮列表
            cur_rad = ttk.Radiobutton(self.vf1, text=self.vsrc[col],  variable=self.vsrc_rbn, value=col+1, command=vsrc_rbn_call)
            cur_rad.place(x=30+col*80, y=4)
            if self.vsrc[col] == '欧冠':     # 小笨之最爱
                cur_rad.configure(state='disabled')  

        # 视频解析接口切换 LabelFrame 2
        self.vf2=tk.LabelFrame(self.video, width=190, height=40)
        self.vf2.grid(row=0,column=1,padx=5, pady=10)
        
        # 解析接口经常失效，找几个能用的延长使用寿命
        self.vf2_lb = tk.Label(self.vf2, text='切换线路: ', font=('微软雅黑', 12), padx=4)
        self.vf2_lb.place(x=10,y=4)

        self.line_var = tk.StringVar(value='Line-1')
        self.line_button = ttk.Button(self.vf2, textvariable=self.line_var,  width=8,  command=self.switchline) #.switch_line
        self.line_button.place(x=94,y=2)
        self.now_line_number = 1


        # 拷入VIP视频链接供观看 LabelFrame 3       
        self.vf3=tk.LabelFrame(self.video, width=610, height=50)
        self.vf3.grid(row=1,column=0,padx=5, pady=5, columnspan=2)

        self.vf3_lb = tk.Label(self.vf3, text='视频链接: ', font=('微软雅黑', 12), padx=4)
        self.vf3_lb.place(x=4,y=8)

        self.vf3_en_v = tk.StringVar()         # value='请拷贝VIP视频链接'
        self.vf3_en = tk.Entry(self.vf3, textvariable=self.vf3_en_v, width=42)
        self.vf3_en.place(x=87,y=10)
        self.vf3_en.bind('<Return>', self.playvideo_e)           # 回车
        #self.vf3_en.bind('<Button-1>', lambda event: self.vf3_en_v.set(''))    

        self.vf3_bn = ttk.Button(self.vf3, text=self.n+"看看",   command=self.playvideo)  
        self.vf3_bn.place(x=488,y=8)
        self.videonum = 0     
        self.playaddr = ''

        # 下载路径选择 LabelFrame 4       
        self.vf4=tk.LabelFrame(self.video, width=610, height=90)
        self.vf4.grid(row=2,column=0,padx=15, pady=5, columnspan=2)
        
        # 下载路径选择
        self.vf4_lb = tk.Label(self.vf4, text='下载路径: ', font=('微软雅黑', 12), padx=8)
        self.vf4_lb.place(x=0,y=8)

        self.path = tk.StringVar()
        #self.path.set(os.path.abspath(os.path.dirname(__file__)))
        self.path.set(os.path.abspath("."))
        self.vf4_en = tk.Entry(self.vf4, textvariable=self.path, width=42)
        self.vf4_en.place(x=87,y=10)
        self.downpath = self.path.get() + '\\' + self.n +'看看' +'\\'

        self.vf4_bn = ttk.Button(self.vf4, text=self.n+"选选", command=self.select_path)  
        self.vf4_bn.place(x=488,y=8)

        # 按序号下载
        self.vf4_lb2 = tk.Label(self.vf4, text='下载序号: ', font=('微软雅黑', 12), padx=8)
        self.vf4_lb2.place(x=0,y=43)
        
        self.vf4_en2_v = tk.StringVar()        # value='输入序号或双击'
        self.vf4_en2 = tk.Entry(self.vf4, textvariable=self.vf4_en2_v, width=15)
        self.vf4_en2.place(x=87,y=46)
        self.vf4_en2.bind('<Return>', self.downloadvideo_e)
        #self.vf4_en2.bind('<Button-1>', lambda event: self.vf4_en2_v.set(''))

        # 复选框 All值为-1 则全部下载
        self.vf4_cbn_v = tk.IntVar()
        self.vf4_cbn_v.set(-2)
        self.vf4_cbn = tk.Checkbutton(self.vf4, text='All', variable=self.vf4_cbn_v, onvalue=-1, offvalue=-2)
        self.vf4_cbn.place(x=250,y=45)

        self.vf4_bn2 = ttk.Button(self.vf4, text=self.n+"下下", command=self.downloadvideo)  
        self.vf4_bn2.place(x=488,y=45)

        # 初始默选电影禁用下载序号等组件
        self.down_config('disabled')

        self.v=WeiVideo()
      
        # 创建电视剧集显示TEXT
    def textcreate(self):
        # 电视剧下载时先将剧集显示到TXT供选择 LabelFrame 5       
        self.vf5=tk.LabelFrame(self.video, width=610, height=325)
        self.vf5.grid(row=3,column=0,padx=15, pady=5, columnspan=2)

        # 显示搜索内容，供按序号下载或全部下载
        self.txt = scrolledtext.ScrolledText(self.vf5, width=62, height=15, padx=10,font=('微软雅黑', 11))
        self.txt.place(x=4,y=10)

    # 从电视剧切换到电影时，去掉TXT组件
    def textdestroy(self):
        self.vf5.destroy()
        self.txt.destroy()

    # 选择电影时不需要下载序号等组件，选电视剧时恢复
    def down_config(self, s):
        self.vf4_lb2.config(state=s)
        self.vf4_en2.config(state=s)
        self.vf4_cbn.config(state=s)

    def switchline(self):
        # 切换下一条线路        
        now_line, self.now_line_number = self.v.switch_line(self.now_line_number)
        self.line_var.set(now_line)
        
    def select_path(self):
        path_ = askdirectory()   # 返回文件夹的路径
        if path_ != "":          # 点击"取消" 输入框会清空路径
            self.path.set(path_.replace("/", "\\"))
        
        self.downpath = self.path.get() + '\\' + self.n +'看看' +'\\'

    # 绑定回车鼠标等事件    
    def playvideo_e(self, event):
        self.playvideo()
    # 观看视频
    def playvideo(self):
        print('1. in playvideo.......')
        # 先输入地址
        if self.vf3_en_v.get() == '':
            msgbox.showwarning("Warning", "请输入VIP视频地址，请检查！")
            return

        if not self.v.play_video(self.vf3_en_v.get()) :
            msgbox.showerror(title='错误', message='视频链接地址无效，请确认！') 

        # 观看时顺便把剧集显示出来
        self.showurl()  
        
        # 地址不变时不重复显示
        self.playaddr = self.vf3_en_v.get()

    # 获取下载URL
    def showurl(self):
        print('2.  in showurl......')

        if self.vf3_en_v.get() == '':
            msgbox.showwarning("Warning", "先输入VIP视频地址，请检查！")
            return

        # 地址不变时不重复显示
        if self.playaddr == self.vf3_en_v.get():            
            return

        # 根据链接搜索下载URL，返回搜索内容供显示
        c,self.videonum=self.v.get_url(self.vf3_en_v.get())    
        if self.videonum == 0:
            c = '\n\t很遗憾，未搜索到结果，请重新搜索。:(' 

        print(c)
        # 如果是电视剧就显示剧集，电影就不显示了
        if self.vsrc_rbn.get() == 2: 
            self.txt.delete(1.0,tk.END)
            self.txt.insert(1.0, c)
            
            # 在搜索结果中序号上加上 下载链接
            for i in range(self.videonum):
                c=str(i+3)    # 歌曲从第三行开始
                # 将结果中序号加链接文字变蓝加下划线
                self.txt.tag_add("link"+c,c+".0",c+".5")
                self.txt.tag_config("link"+c,foreground="blue",underline=True)
                # 绑定鼠标单击事件
                self.txt.tag_bind("link"+c,"<Button-1>", self.arrowclick)
                self.txt.tag_bind("link"+c,"<Enter>",self.showarrowcursor)

    # 当单击链接时开始下载
    def arrowclick(self, event):
        # 获取光标当前位置如10.2，只留行号10, 也即序号为8的歌曲
        no=int(re.match(r'\d+',self.txt.index(tk.CURRENT)).group(0)) 

        count = self.v.download_video(no-2, self.downpath)    # 当前行号去掉前面两行即下载序号
        msgbox.showinfo("Info", "成功下载({})集，请确认！".format(count))

    # 改变鼠标形状
    def showarrowcursor(self, event):
        self.txt.config(cursor="hand2")

    # 事件
    def downloadvideo_e(self, event):
        self.downloadvideo()    
    # 根据输入序号或筛选ALL进行下载
    def downloadvideo(self):
        print('3.  in downloadvideo......')

        num = 1     # 电影默认为数量为1 

        # 如果不观看直接下载则先显示剧集
        self.showurl()
        
        # 异常处理：如果没有搜索或未输入序号，弹窗返回
        if self.videonum == 0:
            msgbox.showwarning("Warning", "未搜索到视频下载地址，抱歉！")
            return

        # 如果是电视剧，则支持复选ALL全部下载、输入单一序号、鼠标单击等方式下载
        if self.vsrc_rbn.get() == 2:    
            if self.vf4_cbn_v.get() != -1 and (self.vf4_en2_v.get() == '' or self.vf4_en2_v.get() == '输入序号或双击'):
                msgbox.showwarning("Warning", "输入剧集序号，请检查！")
                return

            # 如果All复选则全部下载，否则只下选定序号的歌曲。不在范围的弹窗返回
            if self.vf4_cbn_v.get() == -1:
                num=-1
            elif int(self.vf4_en2_v.get())>0 and int(self.vf4_en2_v.get())<=self.videonum+1:
                num=int(self.vf4_en2_v.get())
            else:
                msgbox.showwarning("Warning", "输入序号未在搜索范围，请检查！")
                return

        count = self.v.download_video(num, self.downpath)
        
        msgbox.showinfo("Info", "成功下载({})集，请确认！".format(count))   


if __name__ == '__main__':
    g=Weige()
    g.video.mainloop()
