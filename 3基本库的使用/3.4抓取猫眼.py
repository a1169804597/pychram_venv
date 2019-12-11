#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/9/25 21:27
#@Author :zbwu103
#@File  ：test.py
#@功能：利用requests库和正则表达式来抓取猫眼电影TOP100的相关内容
import requests,re,json,time

def get_one_page(url):
    headers={
        'Host': 'maoyan.com',
        'User - Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    return None
def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?board-img="(.*?)".*?title="(.*?)".*?star">(.*?)</p>.*?"releasetime"(.*?)</p>.*?"integer">(.*?)</i>.*?"fraction">(.*?)</i>',re.S)
    results = re.findall(pattern,html)
    for result in results:
        yield{
            'index':result[0],
            'image':result[1],
            'tiele':result[2],
            'action':result[3].strip()[3:],
            'time':result[4].strip()[5:],
            'score':result[5]+result[6]
        }
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8')as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
def main(offset):
    url='http://maoyan.com/board/4'+'?offset='+str(offset)
    html=get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)
if __name__=='__main__':
    for i in range(10):
        main(i*10)