import requests
import os
import time
import multiprocessing
import json
import sys
import numpy as np
#import urllib.request
from urllib import request
s_dir = 'D:\\dataokill01'
if os.access("D:\\dataokill01", os.F_OK):
    print("文件完整，开始搞事！")
else:
   print("文件不整，已修复")
   os.mkdir("D:\\dataokill01")
time.sleep(0.5)
print("1.键盘输入  2.URL获取（开发中）")
shit=eval(input("请输入获取URL方式:"))
if shit==1:
   urls=input("请输入链接:")#https://i0.hdslb.com/bfs/archive/7e2abc7e4a370f2199d82733786d56fee1899643.png
   nubl=eval(input("请输入次数:"))
   for i in range(nubl):
            headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
               }
            r=requests.get(url=urls,headers=headers)
            if r.status_code == 200:
               print('链接正常')
            if r.status_code != 200:
               print('链接异常,程序已退出!',r)
               sys.exit(0)
            #print(r)
            f=open(r'D:\dataokill01\1.jpg',mode='wb')
            f.write(r.content)
            f.close()
            print('成功刷了',i+1,"次")
if shit==2:
   print("正在通过云端获取链接")
   time.sleep(0.5)
   URL = 'https://api.datao2233.top/index.json'
   def fetch_data(url):
       req = request.Request(url)
       with request.urlopen(req) as f:
        return json.loads(f.read().decode('utf-8')) 
   data = fetch_data(URL)
   urls=data['urls']
   nubls=data['nubl']
   nubl=int(nubls)
   print("成功获取链接",urls,"次数",nubls)
   time.sleep(1)
   for i in range(nubl):
      headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
         }
      r=requests.get(url=urls,headers=headers)
      print(r)
      f=open(r'D:\\dataokill01\1.jpg',mode='wb')
      f.write(r.content)
      f.close()
      print('成功刷了',i+1,"次")

try:
   shutil.rmtree(s_dir)
except (PermissionError, OSError):
   shutil.rmtree(s_dir)
except Exception as error:
   os.system('rd /s/q %s' % s_dir)
print("刷取完成，已删除临时文件")

#鸟码写的跟谢特一样