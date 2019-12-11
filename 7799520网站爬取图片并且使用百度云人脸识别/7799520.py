#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/5/27 23:24
#@Author :zbwu103
#@File  ：7799520.py
#@功能：爬取7799520网站的图片，并用百度智能云给人物图打分

import requests
import jsonpath,os
from urllib.request import urlretrieve
from aip import AipFace
import base64
if not os.path.exists('./img'):
    os.mkdir('./img')
def get_img(page):
    try:
        base_url='http://www.7799520.com/api/user/pc/list/search?marry=1&page='
        url=base_url+str(page)
        response=requests.get(url).json()
        infos=jsonpath.jsonpath(response,'$..list')

        for info in infos[0]:
            # print(info)
            info['username']
            urlretrieve(info[ 'avatar'],'./img'+'/'+info['username']+'.png')
    except:
        print("图片获取错误")
def face_rg(file_path):
    APP_ID = '16363054'
    API_KEY = 'l2NxG0iy9rTiyV3rbhmTwjgB'
    SECRET_KEY = 'mcBPYBTeNiC1xznf9cEH5il8jVtmUCgM'
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)
    with open(file_path, 'rb') as f:
        date = base64.b64encode(f.read())
    image = date.decode()
    options = {}

    imageType = "BASE64"
    options["face_field"] = "beauty"
    """ 调用人脸检测 """
    result=client.detect(image, imageType,options)
    beauty = jsonpath.jsonpath(result, '$..beauty')
    return  beauty
    # return result['result']['face_list'][0]['beauty']
def main():
    for page in range(1,10):
        get_img(page)
    path = r'D:\python\项目\venv\项目操作\img'
    list_path = os.listdir(path)
    # print(list_path)
    # print(len(list_path))
    fss = []
    for i in list_path:
        fs = face_rg(path + '\\' + i)
        fss.append(fs[0])
    # print(fss)
    return list_path,fss

if __name__=='__main__':
    names,datas = main()
    for name,data in zip(names,datas):
        print(name,data)