''' 借用接口，观看视频只需要用三行代码：接口链接+观看链接
    import webbrowser
    url='https://z1.m1907.cn/?jx=https://www.iqiyi.com/v_2baf6bkf2s8.html' 
    webbrowser.open(url)

    下载则需要找到实际地址，比较麻烦
'''

import ffmpy3
from hashlib import md5
import json
from multiprocessing.dummy import Pool as ThreadPool
import os
import re
import requests
import webbrowser
import time
import datetime


class WeiVideo(object):
    def __init__(self):

        self.info_list = []    # 保存下载所需信息
        self.d = Line2()       # 先实现线路二的下载

        # 视频接口时效不定，找了几个接口。线路二可以查看剧集，但有广告
        self.lines = {
            "Line-1": "https://okjx.cc/?url={}",
            "Line-2": "https://z1.m1907.cn/?jx={}",
            "Line-3": "https://jx.618g.com/?url={}",
            "Line-4": "http://www.sfsft.com/admin.php?url={}",
        }
        self.now_line = "Line-1"

    # 切换线路
    def switch_line(self, linenumber):
        # 将字典的key变成一个列表
        line_list = list(self.lines.keys())
        # 线路递增循环
        self.now_line_number = linenumber + 1
        self.now_line_number %= len(line_list)

        # 设置现在的线路, 列表序号从0开始，显示从1开始
        self.now_line = line_list[self.now_line_number-1]

        return self.now_line, self.now_line_number

    
    def play_video(self, url):
        print('4.  in play_video......')

        # 视频接口的完整链接
        video_url = self.lines[self.now_line].format(url)
        
        # 正则表达式判定是否为合法连接
        if not re.match(r'^https?:/{2}\w.+$', url): 
            return False       
        
        # 用浏览器打开网址观看
        webbrowser.open(video_url)

        return True

    # 预留其他线路扩展
    def get_url(self, url) :
        return self.d.line_get_url(url)
    def download_video(self, num, path):
        return self.d.line_download(num, path)

class Line2():
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
                        'Cookie': 'aliyungf_tc=AQAAAFvyfRtP/AIATUWYDheCsQtZUPVB; UM_distinctid=17ca270f330a6-07d8ba249b3ece-b7a1438-b1660-17ca270f33186f',
                        'Referer': 'https://z1.m1907.cn/'}
        
        self.in_url = 'https://a1.m1907.cn/api/v/'

        # query string parameters中的z,s1lig经过MD5加密，每天0点会更新
        self.data_d = 'z={0}&jx={1}&s1ig={2}&g=vod.bun,vod2.bd'

        self.info_list=[]
        self.down_list={}      # 多线程时使用字典保存下载信息

    # request get
    def line_get_rsp(self, url):
        # data_d = {
        #     "z": "5d855143e6fd5d1a252ac6c34b2b7e0f",  
        #     "jx": "{}".format(url),
        #     "s1ig": "11399",                           
        #     "g": "vod.bun,vod2.bd"
        # } 
        p,b = MD5p()    # 参数z/s1ig经过MD5加密，需要模拟加密处理，否则会失效

        try:
            response = requests.get(self.in_url, headers=self.headers, params = self.data_d.format(p,url,b), verify=False) 
            print(response.url)          
            response.raise_for_status()
            response.encoding = 'utf-8'
            
            return response.text
        
        except Exception as err:
            print(err)
            return '请求异常'
 
    def line_get_url(self, url): 
        """ 获取下载m3u8地址
        Parameters
        -----------
        name : url
            输入观看的视频地址
        Returns ：
        --------
        list, int
            内容：供显示；数量：搜索到的数量
        """
        print('4. in line_get_url.....')

        count = 0
        content = ''
        self.info_list=[]

        video_text = self.line_get_rsp(url)
        #print(video_text)

        if video_text == '请求异常':
            return  content, count

        video_list = json.loads(video_text)
        # print(video_list)
        
        v_type = video_list['type']    # 类型：'tv' 'movie'
        self.v_name = video_list['data'][0]['name']      # 视频名称
        v_list = video_list['data'][0]['source']['eps']  # 视频m3u8列表
        
        content = '《' + self.v_name + '》' +'\n'        # text上先显示两行
        content += '-'*90+'\n' 
        
        # 获取显示内容
        for video in v_list:
            eps_name = video['name']
            video_url = video['url']
    
            count += 1
            self.info_list.append([eps_name, video_url])    # 保存信息供下载使用
            content+=eps_name + ':' +'\t'+video_url +'\n'

        # 返回搜索内容以及数量供在界面上显示
        return content, count

    def line_download(self, num, path):
        """ 下载
        Parameters
        -----------
        num : int
            下载视频的序号，指定下载；-1则全部下载
        path : str
            下载保存路径
        Returns ：
        --------
        int
            成功下载数量
        """ 
        print('5. in download.....')

        count = 0
        self.down_list={}

        # 在路径下创建视频名称目录
        self.downpath = path+self.v_name+'\\'
        if not os.path.exists(self.downpath):
            os.mkdir(self.downpath)

        # 全部下载或指定下载时保存下载信息。
        if num == -1:
            for i in range(len(self.info_list)) :   # 
                self.down_list[self.info_list[i][1]] = self.info_list[i][0]
                #if self.savefile(i, downpath) == True:
                count += 1
        else :
            self.down_list[self.info_list[num-1][1]] = self.info_list[num-1][0]
            #if self.savefile(num-1, downpath) == True:
            count += 1
        
        print(self.down_list, count)

        # 开8个线程池
        pool = ThreadPool(8)
        results = pool.map(self.save_file, self.down_list.keys())
        pool.close()
        pool.join()

        print(results)     # 研究下线程返回值
        return count  

    def save_file(self, url):
        print('6. in save_file ......')

        downfile = os.path.join(self.downpath, self.down_list[url]+'.mp4')
        
        # 使用FFmpeg拼接ts
        ffmpy3.FFmpeg(inputs={url: None}, outputs={downfile:None}).run()
            
    # def savefile(self, num, path):
    #     print('in savefile ......')

    #     downfile = os.path.join(path, self.info_list[num][0]+'.mp4')
    #     print(self.info_list[num][1], downfile)
    #     ffmpy3.FFmpeg(inputs={self.info_list[num][1]: None}, outputs={downfile:None}).run()

        return True


''' 模拟网站JS中加密，找不到St()是个啥，猜是MD5算法
    request中的query string parameters：
        "z": "5d855143e6fd5d1a252ac6c34b2b7e0f",    
        "jx": "{}"
        "s1ig": "11399",                       
    
    js文件的定义：
    c = new Date,
    l = c.getTime(),
    u = 6e4 * c.getTimezoneOffset(),
    d = l + u + 36e5 * 8,
    m = new Date(d),
    p = (p = m).getDate() + 9 + 9 ^ 10,
    p = (p = St()(String(p))).substring(0, 10),
    p = St()(p),
    b = m.getDay() + 11397,
    v = "//a1.m1907.cn/api/v/?z=".concat(p, "&jx=").concat(o),
    v += "&s1ig=".concat(b),
'''
def MD5p() :
    lt = datetime.datetime.now()
    ut = datetime.datetime.utcnow()
    o = ((ut.day-lt.day)*24+ut.hour-lt.hour)*60
    #o = (ut.hour-lt.hour)*60

    l = int(time.time()*1000)
    u = int(6e4 * o)            
    d = int(l + u + 36e5 * 8)
    m = time.strptime(time.ctime(d/1000)).tm_mday
    p = str(m+ 9 + 9^10) 
    b = lt.weekday()+1 + 11397

    p=md5(p.encode()).hexdigest()
    p=md5(p[0:10].encode()).hexdigest()

    return p, b