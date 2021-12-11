
import json
import os
import requests
import time
from urllib import parse

class QQMusic(object):
    def __init__(self):
        self.info_list = []

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
        print('search in QQMusic.....')

        count = 0
        content = ''
        self.info_list=[]

        search_url = f'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&' \
                f'new_json=1&remoteplace=txt.yqq.song&searchid=71013496128335959&t=0&' \
                f'aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=30&w={parse.quote(name)}&' \
                f'g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&' \
                f'outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'

        # 爬取网页数据，转换为json数据
        search_text = requests.get(search_url).text
        search_json = json.loads(search_text)
        
        if 'data' not in search_json:
            return  content, count

        song_list = search_json['data']['song']['list']
        
        content = '序号'+'\t'+'音乐名'+'\t'*3+'歌手'+'\t'*2+'专辑'+'\n'
        content += '-'*90+'\n' 
        
        # print('{:*^80}'.format('搜索结果如下'))
        # print('{0:{5}<5}{1:{5}<15}{2:{5}<10}{3:{5}<10}{4:{5}<20}'.format('序号', '歌名', '歌手', '时长(s)', '专辑', chr(12288)))
        # print('{:-^84}'.format('-'))

        for song in song_list:
            singer_name = song['singer'][0]['name']
            song_name = song["title"]
            album_name = song['album']['name']
            mid = song['mid']

            count += 1
            self.info_list.append([mid, song_name, singer_name])

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
        print('download in QQMusic.....')

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

        song_info_url = f'https://u.y.qq.com/cgi-bin/musicu.fcg?&g_tk=5381&loginUin=0&hostUin=0&format=json&' \
                        f'inCharset=utf8&outCharset=utf-8¬ice=0&platform=yqq.json&needNewCode=0&' \
                        f'data=%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method' \
                        f'%22%3A%22GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%223424906048%22%2C%' \
                        f'22calltype%22%3A0%2C%22userip%22%3A%22%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%' \
                        f'22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%' \
                        f'22%3A%223424906048%22%2C%22songmid%22%3A%5B%22{download_info[0]}%22%5D%2C%22songtype%22%3A%' \
                        f'5B0%5D%2C%22uin%22%3A%220%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%' \
                        f'22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A0%2C%22format%22%3A%22json%22%2C%22ct%22%' \
                        f'3A24%2C%22cv%22%3A0%7D%7D'

        # 获取音乐数据并转换为json数据
        song_text = requests.get(song_info_url).text
        qq_music_json = json.loads(song_text)
        if 'req_0' not in qq_music_json:
            return False

        song_purl = qq_music_json['req_0']['data']['midurlinfo'][0]['purl']

        # 获取音乐链接
        song_url = f'https://ws.stream.qqmusic.qq.com/{song_purl}'
        #print(song_url)

        # # 删除Host，否则get失败
        # if 'Host' in self.headers:
        #     del self.headers['Host']
            
        response = requests.get(song_url)
        #print(response)

        if response.status_code != requests.codes.ok:
            return False

        audio_name = download_info[2] + ' - ' + download_info[1]

        print('write file.....')
        with open(os.path.join(path, audio_name) + '.mp3', 'wb') as f:
            f.write(response.content)
        #time.sleep(0.5)

        return True
