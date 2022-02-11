'''
1. 查询余票
    url：https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2022-02-10
         &leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=HHC&purpose_codes=ADULT
    查询地转换字母代号
    url：https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9226
2. 模拟登录
    1). 通过selemium打开一个登录浏览窗口
    2). 防止12306禁止selemium
    3). 点击账号登录，输入用户名密码
    4). 保存图片验证码
    5). 识别验证码的图片
    6). 模拟点击效果，立即登录
    7). 弹出滑动验证码，破解，完成登录
3. 进行订票
    1). 关闭疫情弹窗
    2). 点击首页
    3). 输入购票信息（出发地，到达地，日期）
    4). 点击查询（切换到新的标签页）
    5). 确认弹窗
    6). 选择自己想要的班次，默认使用第二个
    7). 选择乘车人
    8). 选择席别下拉框，选择想要的席位
    9). 提交订单
    10). 确认订单并关闭弹窗（至此订单成功，请在半小时内完成出票）
'''

import re
import time
import base64
import urllib3
import requests
from selenium.webdriver import Chrome, ActionChains    # Alt+Enter 快速导入
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

urllib3.disable_warnings()

username = "xxxxxxxxx"
password = "xxxxxxxx"
name = "xxx"
seat_name = "硬卧（￥389.0）"

class LeftQuery:

    def __init__(self):
        self.station_url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9226"
        self.query_url = "https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date={0}" \
                         "&leftTicketDTO.from_station={1}&leftTicketDTO.to_station={2}&purpose_codes=ADULT"
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/97.0.4692.99 Safari/537.36",
            'Cookie': '_uab_collina=164389871932125908140505; JSESSIONID=BE3F5D556C7527CB9266E806AE204EF5; '
                      'BIGipServerpool_passport=182714890.50215.0000; guidesStatus=off; highContrastMode=defaltMode; '
                      'cursorStatus=off; RAIL_EXPIRATION=1644180601372; '
                      'RAIL_DEVICEID=WHnVwkDWoBO7Zcszs4mBOqfvAtJgxTrOKC75FxYc3YJpWEN65RB19Dh85tR'
                      '_tG9ASy0ziR9DVMmz2FC8gurAOx2tZ076nCWM1k9537EOrmrmo_6Ty5mvF2n6x6V7jl_AtNra_E8Or9M2OOkCKJMUPwx1aeNICrNq; '
                      'route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; '
                      '_jc_save_toStation=%u547C%u548C%u6D69%u7279%2CHHC; _jc_save_wfdc_flag=dc; _jc_save_fromDate=2022-02-04; '
                      'BIGipServerotn=4090953994.24610.0000; _jc_save_toDate=2022-02-04'
        }

    def get_station_name(self, station):
        '''将查询车站名（汉字）转换为字母代号'''
        response = requests.get(url=self.station_url, headers=self.headers, verify=False).text
        # print(response)

        result = response.split('@')[1:]
        temp_dict = {}
        for i in result:
            temp_list = i.split('|')
            temp_dict[temp_list[1]] = i.split('|')[2]

        return temp_dict[station]

    def query(self, from_station, to_station, date):
        '''查询余票'''
        fromstation = self.get_station_name(from_station)
        tostation = self.get_station_name(to_station)

        response = requests.get(url=self.query_url.format(date, fromstation, tostation), headers=self.headers, verify=False).json()
        result = response['data']['result']
        # print(result)

        if result is None:
            print('Sorry,,,,No query result')
            exit()
        else:
            print(date + ' ' + from_station + '->' + to_station + " 查询成功!\n ")
            for i in result:
                info = i.split("|")
                if info[0] != '' and info[0] != "null":
                    print(info[3] + "车次还有余票.")
                    print("出发时间:" + info[8] + " 到达时间:" + info[9] + " 历时时长:" + info[10] + ' ', end='')
                    # 商务座32 一等座31 二等座30 动卧33 软卧23 硬卧28 硬座29 无座26
                    seat = {
                        21:'高级软卧',
                        23:'软卧',
                        26:'无座',
                        28:'硬卧',
                        29:'硬座',
                        30:'二等座',
                        31:'一等座',
                        32:'商务座',
                        33:'动卧'
                    }
                    for j in seat.keys():
                        if info[j] != '无' and info[j] != '':
                            if info[j] == '有':
                                print(seat[j] + ':有票 ', end='')
                            else:
                                print(seat[j] + ":有" + info[j] + '张票 ', end='')
                    print('\n')

        return result

def discern_captcha():
    ''' 通过第三方接口识别图片验证码 '''

    url_captcha = "http://littlebigluo.qicp.net:47720/"
    files = {
        "pic_xxfile": open("pic.png", "rb")
    }

    res = requests.post(url=url_captcha, files=files, verify=False)
    img_num = re.search("<B>(.*?)</B>", res).group(1).replace(" ",",")

    img_num_list = img_num.split(",")
    answer_list = []
    # 图片坐标
    coordinate = {
         '1': (31,35),
         '2': (116,46),
         '3': (191,24),
         '4': (243,50),
         '5': (22,114),
         '6': (117,94),
         '7': (167,120),
         '8': (251,105),
        }

    # 循环遍历，构建数据结构[[x1,y1], [x2,y2]...]
    for i in img_num_list:
        x_y = []
        x_y.append(coordinate[i][0])
        x_y.append(coordinate[i][1])
        answer_list.append(x_y)

    return answer_list

def login():

    # 1. 通过selemium打开一个登录浏览窗口
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://kyfw.12306.cn/otn/resources/login.html")

    # 2. 防止12306禁止selemium
    script = "Object.defineProperty(navigator, 'webdriver', {get:()=>undefined,});"
    driver.execute_script(script)
    time.sleep(1)

    # 3. 点击账号登录，输入用户名密码
    # driver.find_element_by_xpath("/html/body/div[2]/div[2]/ul/li[2]/a").click()
    # 输入账号密码
    driver.find_element_by_id("J-userName").send_keys(username)
    time.sleep(1)
    driver.find_element_by_id("J-password").send_keys(password)
    time.sleep(1)

    # 4. 保存图片验证码
    # img = driver.find_element_by_id("J-loginImg")
    # pic_url = img.get_attribute("src")
    # pic = base64.b64decode(pic_url.split(',')[1])  # 去除逗号前的"data:image/jpg;base64," 无用数据
    # with open("pic.png","wb") as f:
    #     f.write(pic)

    # 5. 识别验证码的图片
    # answer_list = discern_captcha()
    # for l in answer_list:
    #     x = l[0]
    #     y = l[1]
    #
    #     ActionChains(driver).move_to_element_with_offset(img, x+10, y+30).click().perform()
    #     time.sleep(1)

    # 6. 模拟点击效果，立即登录
    driver.find_element_by_id("J-login").click()
    time.sleep(3)

    # 7. 弹出滑动验证码，破解，完成登录
    span = driver.find_element_by_id("nc_1_n1z")
    action = ActionChains(driver)
    action.click_and_hold(span)
    action.move_by_offset(350, 0).perform()  # x轴移动350， y轴移动为0
    time.sleep(5)

    return driver

def order(from_station, to_station, date):

    # 1. 余票查询
    query = LeftQuery()
    query.query(from_station, to_station, date)

    # 2. 登录
    driver = login()

    # 1). 关闭疫情弹窗
    driver.find_element_by_class_name("ok").click()
    #driver.find_element_by_xpath("/html/body/div[2]/div[2]/ul/li[2]/a").click()
    time.sleep(1)

    # 2). 点击首页
    driver.find_element_by_id("J-index").click()
    time.sleep(1)

    # 3). 输入购票信息（出发地，到达地，日期）
    # 输入出发地
    from_input = driver.find_element_by_id("fromStationText")
    from_input.click()
    from_input.send_keys(from_station)
    from_input.send_keys(Keys.ENTER)  # 回车失去焦点
    time.sleep(1)
    # 输入到达地
    to_input = driver.find_element_by_id("toStationText")
    to_input.click()
    to_input.send_keys(to_station)
    to_input.send_keys(Keys.ENTER)
    time.sleep(1)
    # 输入日期
    driver.execute_script('document.getElementById("train_date").removeAttribute("autocomplete")')  # 取消标签只读模式
    date_input = driver.find_element_by_id("train_date")
    date_input.clear()
    date_input.click()
    date_input.send_keys(date)
    # 回车无法失去焦点，想办法：点击”车票“让其失去焦点
    driver.find_elements_by_class_name("active")[1].click()
    time.sleep(1)

    # 4). 点击查询（切换到新的标签页）
    driver.find_element_by_id("search_one").click()
    time.sleep(1)
    # 打开一个新页面，窗口需要切换
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(1)

    # 5). 确认弹窗
    # driver.find_elements_by_class_name("qd_closeDefaultWarningWindowDialog_id").click()
    # time.sleep(1)

    # 6). 选择自己想要的班次，默认使用第二个
    driver.find_elements_by_class_name("btn72")[1].click()
    time.sleep(1)

    # 7). 选择乘车人
    # driver.find_element_by_id("normalPassenger_0").click()
    driver.find_element_by_xpath("//div//ul[@id='normal_passenger_id']//li//label[contains(text(), %s)]" %name).click()
    time.sleep(1)

    # 8). 选择席别下拉框，选择想要的席位
    seat_type = driver.find_element_by_id("seatType_1")
    seat_type.click()
    time.sleep(1)

    Select(seat_type).select_by_visible_text(seat_name)
    time.sleep(1)

    # 9). 提交订单
    driver.find_element_by_id("submitOrder_id").click()
    time.sleep(1)

    # 10). 确认订单并关闭弹窗（至此订单成功，请在半小时内完成出票）
    driver.find_element_by_id("qr_submit_id").click()
    time.sleep(1)

    time.sleep(3600)

if __name__ == '__main__':
    # l_q = LeftQuery()
    order('上海', '呼和浩特', '2022-02-11')


