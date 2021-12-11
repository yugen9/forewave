## 冬夜，微醺，刚哥想听歌：
## 于是刚哥开始学习：人生苦短，我用python

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as msgbox
from tkinter import scrolledtext
from tkinter.filedialog import askdirectory
import os
import re

from wangyiyun.wyy import WyyMusic
from kuwo.kw import KwMusic
from kugou.kg import KgMusic
from QQ.QQ import QQMusic

#from temp.tmp import  WyyMusic,KwMusic,KgMusic,QQMusic 

# main : tkinter图形界面  1. 选择音乐来源（网易云酷狗酷我QQ） 2. 搜索下载
# LableFrame + grid, 各组件place确定其位置
class Gangge():
    def __init__(self):
        # 人名
        self.n = '刚哥'
        
        # 选择 网易云，酷狗，酷我，QQ 音乐
        self.m = [WyyMusic, KgMusic, KwMusic, QQMusic]
        self.msic = self.m[0]() 

        self.music = tk.Tk()
        self.music.title('冬夜，微醺，'+self.n+'想听歌：')
        
        # 选择音乐源以及音乐品质 download LabelFrame 1
        self.dlf1=tk.LabelFrame(self.music, width=600, height=90, text=self.n+'选选', font=('黑体', 13), fg='blue')
        self.dlf1.grid(row=0,column=0,padx=15, pady=10)

        self.dmlbs = tk.Label(self.dlf1, text='音乐来源: ', font=('微软雅黑', 12), padx=4)
        self.dmlbs.place(x=0,y=0)

        # 定义音乐来源
        self.dmsrc = ['网易云', '酷狗', '酷我', 'QQ']

        # 单选按钮回调函数
        def radmsrc_call():
            self.msic = self.m[self.radmsrc.get()-1]()    # 根据单选确定网易云等来源

        self.radmsrc = tk.IntVar()
        self.radmsrc.set(1)
        for col in range(len(self.dmsrc)):   # 创建单选按钮列表
            cur_rad = ttk.Radiobutton(self.dlf1, text=self.dmsrc[col],  variable=self.radmsrc, value=col+1, command=radmsrc_call)
            cur_rad.place(x=110+col*80, y=0)
            # if self.dmsrc[col] == 'QQ':     # QQ音乐待实现
            #     cur_rad.configure(state='disabled')    

        # 待实现 无损音乐 等的筛选
        self.dmlbt = tk.Label(self.dlf1, text='音乐类型: ', font=('微软雅黑', 12), padx=4)
        self.dmlbt.place(x=0,y=30)

        # 定义音质类型 : 流畅音质  128k  高频音质  192k 超品音质  320k
        self.dmtype = ['All', '无损音质']
        # 单选按钮回调函数，预留
        def radmtype_call():
            pass
        self.radmt = tk.IntVar()
        self.radmt.set(1)
        for col in range(len(self.dmtype)):  
            cur_rad1 = ttk.Radiobutton(self.dlf1, text=self.dmtype[col],  variable=self.radmt, value=col+1, command=radmtype_call)
            cur_rad1.place(x=110+col*80, y=30) 
            if self.dmtype[col] == '无损音质':    # 以后有空再实现
                cur_rad1.configure(state='disabled')     

        # 搜索并下载音乐或歌手的音乐 download LabelFrame 2       
        self.dlf2=tk.LabelFrame(self.music, width=600, height=500, text=self.n+'下下', font=('黑体', 13), fg='blue')
        self.dlf2.grid(row=1,column=0,padx=15, pady=5)

        # 搜索音乐或歌手
        self.dmlbdc = tk.Label(self.dlf2, text='音乐/歌手: ', font=('微软雅黑', 12), padx=4)
        self.dmlbdc.place(x=0,y=10)

        self.dme1t = tk.StringVar(value='下载的音乐名或歌手名')         # value='下载的音乐名或歌手名'
        self.dme1 = tk.Entry(self.dlf2, textvariable=self.dme1t, width=30)
        self.dme1.place(x=110,y=10)
        self.dme1.bind('<Return>', self.music_s)           # 回车
        self.dme1.bind('<Button-1>', lambda event: self.dme1t.set(''))    # 鼠标进入

        self.dme1a = ttk.Button(self.dlf2, text="搜索", command=self.music_search)  
        self.dme1a.place(x=480,y=10)
        self.songnum = 0    # 搜索到歌曲的数量 
        
        # 下载路径选择
        self.dmlbd1 = tk.Label(self.dlf2, text='下载路径: ', font=('微软雅黑', 12), padx=9)
        self.dmlbd1.place(x=0,y=50)

        self.path = tk.StringVar()
        #self.path.set(os.path.abspath(os.path.dirname(__file__)))
        self.path.set(os.path.abspath("."))
        self.dme2 = tk.Entry(self.dlf2, textvariable=self.path, width=40)
        self.dme2.place(x=110,y=52)
        self.downpath = self.path.get() + '\\' + self.n +'听听'

        self.dme2a = ttk.Button(self.dlf2, text="路径选择", command=self.select_path)  
        self.dme2a.place(x=480,y=50)

        # 按序号下载
        self.dmlbd2 = tk.Label(self.dlf2, text='下载序号: ', font=('微软雅黑', 12), padx=9)
        self.dmlbd2.place(x=0,y=90)
        
        self.dme3n = tk.StringVar(value='要下载歌曲序号')        # value='要下载歌曲序号'
        self.dme3 = tk.Entry(self.dlf2, textvariable=self.dme3n, width=15)
        self.dme3.place(x=110,y=90)
        self.dme3.bind('<Return>', self.music_d)
        self.dme3.bind('<Button-1>', lambda event: self.dme3n.set(''))

        # 复选框 All值为-1 则全部下载
        self.dmckn = tk.IntVar()
        self.dmckn.set(-2)
        self.dmck = tk.Checkbutton(self.dlf2, text='All', variable=self.dmckn, onvalue=-1, offvalue=-2)
        self.dmck.place(x=270,y=90)

        self.dme3a = ttk.Button(self.dlf2, text="下载", command=self.music_download)  
        self.dme3a.place(x=480,y=90)

        # 显示搜索内容，供按序号下载或全部下载
        self.txt = scrolledtext.ScrolledText(self.dlf2, width=61, height=18, padx=10,font=('微软雅黑', 11))
        self.txt.place(x=0,y=130)

    # 绑定回车鼠标等事件    
    def music_s(self, event):
        self.music_search()
    # 根据输入的音乐名或歌手名进行搜索
    def music_search(self):
        if self.dme1t.get() == '':
            msgbox.showwarning("Warning", "请输入歌曲名或歌手名，请检查！")
            return

        # 根据音乐名或歌手名及音乐品质搜索，返回搜索内容
        c,self.songnum=self.msic.search(self.dme1t.get(), self.radmt.get())    
        if self.songnum == 0:
            c = '\n\t很遗憾，未搜索到结果，请重新搜索。:(' 
            
        self.txt.delete(1.0,tk.END)
        self.txt.insert(1.0, c)
        
        # 在搜索结果中序号上加上 下载链接
        for i in range(self.songnum):
            c=str(i+3)    # 歌曲从第三行开始
            # 将结果中序号加链接文字变蓝加下划线
            self.txt.tag_add("link"+c,c+".0",c+".2")
            self.txt.tag_config("link"+c,foreground="blue",underline=True)
            # 绑定鼠标单击事件
            self.txt.tag_bind("link"+c,"<Button-1>", self.arrow_click)
            self.txt.tag_bind("link"+c,"<Enter>",self.show_arrow_cursor)

    # 当单击链接时开始下载
    def arrow_click(self, event):
        # 获取光标当前位置如10.2，只留行号10, 也即序号为8的歌曲
        no=int(re.match(r'\d+',self.txt.index(tk.CURRENT)).group(0)) 

        count = self.msic.download(no-2, self.downpath)    # 当前行号去掉前面两行即歌曲序号
        msgbox.showinfo("Info", "成功下载({})首，请确认！".format(count))

    # 改变鼠标形状
    def show_arrow_cursor(self, event):
        self.txt.config(cursor="hand2")

    def music_d(self, event):
        self.music_download()    
    # 根据输入序号或多选ALL进行下载
    def music_download(self):     
        # 异常处理：如果没有搜索或未输入序号，弹窗返回
        if self.songnum == 0:
            msgbox.showwarning("Warning", "请先搜索歌曲，请检查！")
            return

        if self.dmckn.get() != -1 and self.dme3.get() == '':
            msgbox.showwarning("Warning", "请输入歌曲序号，请检查！")
            return

        # 如果All复选则全部下载，否则只下选定序号的歌曲。不在范围的弹窗返回
        if self.dmckn.get() == -1:
            num=-1
        elif int(self.dme3.get())>0 and int(self.dme3.get())<=self.songnum:
            num=int(self.dme3.get())
        else:
            msgbox.showwarning("Warning", "输入序号未在搜索范围，请检查！")
            return

        count = self.msic.download(num, self.downpath)
        
        msgbox.showinfo("Info", "成功下载({})首，请确认！".format(count))   

    def select_path(self):
        path_ = askdirectory()   # 返回文件夹的路径
        if path_ != "":          # 点击"取消" 输入框会清空路径
            self.path.set(path_.replace("/", "\\"))
        
        self.downpath = self.path.get() + '\\' + self.n +'听听'


if __name__ == '__main__':
    g=Gangge()
    g.music.mainloop()
