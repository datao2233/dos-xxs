import requests
import os
import time
import multiprocessing
import ssl

s_dir = 'D:\\dataokill01'
if os.access("D:\\dataokill01", os.F_OK):
    print("文件完整，开始搞事！")
else:
   print("文件不整，已修复")
   os.mkdir("D:\\dataokill01")
#while True:
for i in range(15):
      ssl._create_default_https_context = ssl._create_unverified_context
      url='https://s1.hdslb.com/bfs/static/blive/blfe-message-web/static/img/infocenterbg.a1a0d152.jpg'
      headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
         }
      r=requests.get(url=url,headers=headers)
      print(r)
      f=open(r'D:\\dataokill01\1.jpg',mode='wb')
      f.write(r.content)
      f.close()
      print('成功刷了',i+1,"次")
try:
	shutil.rmtree(s_dir)
except (PermissionError, OSError):
	time.sleep(1)
	shutil.rmtree(s_dir)
except Exception as error:
	os.system('rd /s/q %s' % s_dir)
print("刷取完成，已删除临时文件")
#鸟码写的跟谢特一样
