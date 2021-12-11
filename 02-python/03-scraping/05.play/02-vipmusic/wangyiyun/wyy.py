
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import json
import os
import random
import re
import requests
import time


# 搜索，下载请求
class WyyMusic(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        self.id_url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
        self.song_url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
        
        self.encrypt = EncryptText()
        self.info_list = []

    def get_html(self, url, method='GET', from_data=None):
        try:
            if method == 'GET':
                response = requests.get(url, headers=self.headers)
            else:
                response = requests.post(url, from_data, headers=self.headers)
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
        count = 0         # 搜索到歌曲的数量
        content = ''      # TEXT中显示内容
        self.info_list=[] # 利用给下载的数据
       
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
        id_text = self.get_html(self.id_url, method='POST', from_data=id_from_data)        
     
        if id_text == '请求异常' :     #or 'result' not in json.loads(id_text)
            return  content, count
        
        ids_list = json.loads(id_text)['result']['songs']
       
        content = '序号'+'\t'+'音乐名'+'\t'*3+'歌手'+'\t'*2+'专辑'+'\n'
        content += '-'*90+'\n'
        #print('{:*^80}'.format('搜索结果如下'))
        #print('{0:{5}<5}{1:{5}<20}{2:{5}<10}{3:{5}<10}{4:{5}<20}'.format('序号', '歌名', '歌手', '时长(s)', '专辑', chr(12288)))
        #print('{:-^84}'.format('-'))
        for id_info in ids_list:
            song_name = id_info['name']
            id = id_info['id']
            #time = id_info['dt'] // 1000
            album_name = id_info['al']['name']
            #picture_url = id_info['al']['picUrl']
            singer = id_info['ar'][0]['name']
            
            count += 1
            self.info_list.append([id, song_name, singer])
            content+=str(count)+'\t'+song_name[:10] +'\t'*3+singer[:10]+'\t'*2+album_name[:7]+'\n'
            
            #print('{0:{5}<5}{1:{5}<20}{2:{5}<10}{3:{5}<10}{4:{5}<20}'.format(count, song_name, singer, time, album_name, chr(12288)))       
        #print('{:*^80}'.format('*'))
        # 返回供TEXT显示的内容及数量
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
        print('download in WyyMusic.....')
        # 下载成功的数量
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
        #print('in savefile ......')
        download_info = self.info_list[num]
        song_d = {
            "ids": str([download_info[0]]),
            "level": "standard",
            "encodeType": "aac",
            "csrf_token": ""
        } 

        song_from_data = self.encrypt.resultEncrypt(str(song_d))
        song_text = self.get_html(self.song_url, method='POST', from_data=song_from_data)
        #print(song_text)
        
        if song_text == '请求异常' or 'data' not in json.loads(song_text):    # 
            print('出错了！')
            return False
        
        music_url = json.loads(song_text)['data'][0]['url']
        #print(music_url)  

        response = requests.get(music_url, headers=self.headers)
        if response.status_code != requests.codes.ok:
            return False

        fn = download_info[2] + '-' + download_info[1]
        # 去除文件名中乱字符
        filename = re.compile(u'[^0-9a-zA-Z\u4e00-\u9fa5.\-]+', re.UNICODE).sub('', fn)
        with open(os.path.join(path, filename) + '.mp3', 'wb') as f:
            f.write(response.content)
        time.sleep(0.5)

        return True

# 模拟网易云的加密处理
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



