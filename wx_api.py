#!/usr/bin/env python
# coding=utf-8
import sys
import json
import werobot
from pdb import set_trace

reload(sys)  
sys.setdefaultencoding('utf8')
import requests
#APPID='wx841340fe07dd3028'
#APPSECRET="292fa5f527bd225fc4b0ada4aa82f289"
APPID='wxfd83bb5bc4870588'
APPSECRET='fe5a69a09e405ddc8f29b8f7ba9022d9'
def get_access_token():
    url="https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={APPSECRET}".format(APPID=APPID,APPSECRET=APPSECRET)
    json = requests.get(url).json()
    return json['access_token']
def get_ip():
    
    access_token = get_access_token()

    #access_token='CLuCCB4yxS7Ce5jXask5DQCUXInuZZD6WgAkVOJ-sdOT9PdBLyQNk3BRZGyOrQR72-cyj4HfCJ8JR0LhBRNYJbkMY3fgak7l7x0pLNDrMNzsbYLyeTQm9OF9fjQx2_U8RURcAJAGJG'
    #print access_token
    #url ="https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token=%s"%(access_token)
    #get_data = requests.get(url)
    #print get_data.json()
    return access_token
def set_menu():
    access_token = "7Pg637E_gyj1UM8OKbi5eH5S3Mtm5Zk8Eat_KiClNgTaqnOx7jm79NXmp6To6EGjI_k5I2jMiLWa12ZMltg190xeECj6SRDRppbTv1Taob0FOMjAGALUS"
    #access_token = get_access_token()
    #print access_token
    url=" https://api.weixin.qq.com/cgi-bin/menu/create?access_token={access_token}".format(access_token=access_token)
    menus = {"button": [{"name": "扫码1", "sub_button": [{"type": "scancode_waitmsg", "name": "扫码带提示", "key": "rselfmenu_0_0", "sub_button": [ ]}, {"type": "scancode_push", "name": "扫码推事件", "key": "rselfmenu_0_1", "sub_button": [ ]}]}, {"name": "发图", "sub_button": [{"type": "pic_sysphoto", "name": "系统拍照发图", "key": "rselfmenu_1_0", "sub_button": [ ] }, {"type": "pic_photo_or_album", "name": "拍照或者相册发图", "key": "rselfmenu_1_1", "sub_button": [ ] }, {"type": "pic_weixin", "name": "微信相册发图", "key": "rselfmenu_1_2","sub_button": [ ]}]}]}
    postData = requests.post(url,data=json.dumps(menus, ensure_ascii=False))
    print postData.json()


def test():
    token="NageLxLS32W0OyeWXtJoxrcax841uE8k-8TGPR8oOpCkmkdAGU-_gpQslFvJqqqc_agPQlU4Sbt8vnNyissXxqvyr7fncup-y7Rty5Mbe1EFMhHUGYZqJu4CRl6yN7RDTWFeADAFIR"
    robot = werobot.WeRoBot(token=token)

    @robot.handler
    def hello(message):
        return 'Hello World!'

    # 让服务器监听在 0.0.0.0:80
    robot.config['HOST'] = '0.0.0.0'
    robot.config['PORT'] = 80
    robot.run()


if __name__=='__main__':
    #print get_access_token()
    #get_ip()
    #access_token='CLuCCB4yxS7Ce5jXask5DQCUXInuZZD6WgAkVOJ-sdOT9PdBLyQNk3BRZGyOrQR72-cyj4HfCJ8JR0LhBRNYJbkMY3fgak7l7x0pLNDrMNzsbYLyeTQm9OF9fjQx2_U8RURcAJAGJG'
    #set_menu()
    test()
