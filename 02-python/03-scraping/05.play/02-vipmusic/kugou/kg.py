
from hashlib import md5
import json
import os
import requests
import re
import time
from urllib import parse


class KgMusic(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        self.info_list = []

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
        signature = new_md5.hexdigest()
        url = 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&keyword={0}' \
              '&page=1&pagesize=30&bitrate=0&isfuzzy=0&tag=em&inputtype=0&platform=WebFilter&userid=-1' \
              '&clientver=2000&iscorrection=1&privilege_filter=0&srcappid=2919&clienttime={1}&' \
              'mid={2}&uuid={3}&dfid=-&signature={4}'.format(parse.quote(text), k, k, k, signature.upper())
        return url

    def get_html(self, url):
        # 加一个cookie
        cookie = 'kg_mid=68aa6f0242d4192a2a9e2b91e44c226d; kg_dfid=4DoTYZ0DYq9M3ctVHp0cBghm; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1618922741,1618923483; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1618924198'.split(
            '; ')
        cookie_dict = {}
        for co in cookie:
            co_list = co.split('=')
            cookie_dict[co_list[0]] = co_list[1]
        try:
            response = requests.get(url, headers=self.headers, cookies=cookie_dict, verify=False)
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

        search_url = self.MD5Encrypt(name)

        search_text = self.get_html(search_url)
        
        if search_text == '请求异常' or 'data' not in json.loads(search_text[12:-2]):
            return  content, count

        # print('{:*^80}'.format('搜索结果如下'))
        # print('{0:{5}<5}{1:{5}<15}{2:{5}<10}{3:{5}<10}{4:{5}<20}'.format('序号', '歌名', '歌手', '时长(s)', '专辑', chr(12288)))
        # print('{:-^84}'.format('-'))
        song_list = json.loads(search_text[12:-2])['data']['lists']    # 去除callback123()
        #print(song_list)

        content = '序号'+'\t'+'音乐名'+'\t'*3+'歌手'+'\t'*2+'专辑'+'\n'
        content += '-'*90+'\n' 

        for song in song_list:
            #print(song)
            #print('^'*58)
            singer_name = song['SingerName']
            # <em>本兮</em> 正则提取
            # 先匹配'</em>'这4中字符, 然后将其替换
            pattern = re.compile('[</em>]')
            singer_name = re.sub(pattern, '', singer_name)
            song_name = song['SongName']
            song_name = re.sub(pattern, '', song_name)
            album_name = song['AlbumName']
            album_id = song['AlbumID']
            # 时长
            #duration = song['Duration']
            file_hash = song['FileHash']
            #file_size = song['FileSize']

            # 音质为HQ, 高品质
            hq_file_hash = song['HQFileHash']
            #hq_file_size = song['HQFileSize']

            # 音质为SQ, 超品质, 即无损, 后缀为flac
            sq_file_hash = song['SQFileHash']
            #sq_file_size = song['SQFileSize']

            # MV m4a
            #mv_hash = song['MvHash']
            #m4a_size = song['M4aSize']

            count += 1
            self.info_list.append([file_hash, hq_file_hash, sq_file_hash, album_id])
            content+=str(count)+'\t'+song_name[:10]+'\t'*3+singer_name[:10]+'\t'*2+album_name[:7]+'\n'

        #     print('{0:{5}<5}{1:{5}<15}{2:{5}<10}{3:{5}<10}{4:{5}<20}'.format(count, song_name, singer_name, duration, album_name,chr(12288)))

        # print('{:*^80}'.format('*'))
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
        print('download in KgMusic.....')

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
        song_info_url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={0}&mid=68aa6f0242d4192a2a9e2b91e44c226d&album_id={1}'.format(download_info[0], download_info[3])
        
        #print(download_info[0], download_info[2], download_info[2])
        song_text = self.get_html(song_info_url)
        #print(song_text)

        if song_text == '请求异常' or 'data' not in json.loads(song_text):
            print('出错了！')
            return False

        text = json.loads(song_text)['data']
        audio_name = text['audio_name']
        play_url = text['play_url']
        #print(play_url, audio_name)

        response = requests.get(play_url, headers=self.headers)
        if response.status_code != requests.codes.ok:
            return False

        with open(os.path.join(path, audio_name) + '.mp3', 'wb') as f:
            f.write(response.content)
        time.sleep(0.5)

        return True

