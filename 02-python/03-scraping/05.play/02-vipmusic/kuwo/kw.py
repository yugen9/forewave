
import json
import os
import requests
import time
from urllib import parse



class KwMusic(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                        'Cookie': '_ga=GA1.2.136730414.1610802835; _gid=GA1.2.80092114.1621072767; Hm_lvt_cdb524f'
                                  '42f0ce19b169a8071123a4797=1621072767; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797'
                                  '=1621073279; _gat=1; kw_token=C713RK6IJ8J',
                        'csrf': 'C713RK6IJ8J',
                        'Host': 'www.kuwo.cn',
                        'Referer': ''}
        
        # 搜索结果
        self.info_list = []

    def get_html(self, url, search_key=None):
        if 'mid' not in url:
            self.headers['Referer'] = 'http://www.kuwo.cn/search/list?key=' + search_key
        else:
            #del self.headers['Referer']
            #del self.headers['csrf']
            pass
        try:
            response = requests.get(url, headers=self.headers, verify=False)
            response.raise_for_status()
            response.encoding = 'utf-8'
            return response.text
        except Exception as err:
            print(err)
            return '请求异常'
 
    def search(self, name, type): 
        """ 搜索
        Parameters
        -----------
        name : str
            搜索的歌曲名或歌手名
        type : 
            歌曲音质类型，预留
        Returns ：
        --------
        list, int
            内容：供显示；数量：搜索到的数量
        """
        count = 0
        content = ''
        self.info_list=[]

        search_key = parse.quote(name)
        # pn表示页数, 默认一页30条歌曲信息
        search_url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=50'.format(search_key)
        search_text = self.get_html(search_url, search_key)
        #print(search_text)

        if search_text == '请求异常' or 'data' not in json.loads(search_text):
            return  content, count

        song_list = json.loads(search_text)['data']['list']
        
        content = '序号'+'\t'+'音乐名'+'\t'*3+'歌手'+'\t'*2+'专辑'+'\n'
        content += '-'*90+'\n' 
        
        # print('{:*^80}'.format('搜索结果如下'))
        # print('{0:{5}<5}{1:{5}<15}{2:{5}<10}{3:{5}<10}{4:{5}<20}'.format('序号', '歌名', '歌手', '时长(s)', '专辑', chr(12288)))
        # print('{:-^84}'.format('-'))

        for song in song_list:
            singer_name = song['artist']
            song_name = song['name']
            album_name = song['album']
            rid = song['rid']
            #time_str = get_songtime(song['duration'])

            count += 1
            self.info_list.append([rid, song_name, singer_name])
            content+=str(count)+'\t'+song_name[:10]+'\t'*3+singer_name[:10]+'\t'*2+album_name[:7]+'\n'

        #     print('{0:{5}<5}{1:{5}<20}{2:{5}<10}{3:{5}<10}{4:{5}<20}'.format(count, song_name, singer_name, time_str, album_name, chr(12288)))
        # print('{:*^80}'.format('*'))

        # 返回搜索内容以及数量，供下载判断以及显示在界面上
        return content, count

    def download(self, num, path):
        """ 下载
        Parameters
        -----------
        num : int
            搜索的歌曲的序号，指定下载；-1则全部下载
        path : str
            下载保存路径
        Returns ：
        --------
        int
            成功下载数量
        """ 
        print('download in KwMusic.....')

        count = 0

        if not os.path.exists(path):
            os.mkdir(path)

        if num == -1:
            for i in range(len(self.info_list)):
                if self.savefile(i, path) == True:
                    count += 1
        elif self.savefile(num-1, path)== True:
            count +=1
        
        return count  
             
    def savefile(self, num, path):
        print('in savefile ......')
        download_info = self.info_list[num]
        # 流畅音质  128k  高频音质  192k 超品音质  320k
        #song_info_url = 'http://www.kuwo.cn/url?rid={0}&type=convert_url3&br=128kmp3'.format(download_info[0])
        song_info_url = 'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={0}&type=music&httpsStatus=1&reqId=002569b1-3d2c-11ec-84cc-919fce62ea2e%20Request%20Method:%20GET'.format(download_info[0])
        
        song_text = self.get_html(song_info_url)
        #print(song_text)
        if song_text == '请求异常' or 'data' not in json.loads(song_text):
            print('出错了！')
            return False

        song_url = json.loads(song_text)['data']['url']

        # 删除Host，否则get失败
        if 'Host' in self.headers:
            del self.headers['Host']

        response = requests.get(song_url, headers=self.headers)

        if response.status_code != requests.codes.ok:
            return False

        audio_name = download_info[2] + ' - ' + download_info[1]
        print('write file.....')
        with open(os.path.join(path, audio_name) + '.mp3', 'wb') as f:
            f.write(response.content)
        #time.sleep(0.5)

        return True

def get_songtime(time_str):
    minutes, seconds = divmod(int(time_str), 60)
    result = str(minutes).zfill(2) + ':' + str(seconds).zfill(2)
    return result

# def precess_time(func):
#     def wrapper(*args):
#         minutes, seconds = divmod(int(args[0]), 60)
#         result = str(minutes).zfill(2) + ':' + str(seconds).zfill(2)
#         return result

#     return wrapper

# @precess_time
# def get_songtime(time_str):
#     return time_str

