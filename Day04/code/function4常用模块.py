"""
 @Time    : 2022/7/17 16:52
 @Author  : Xyan9
 @File    : function4常用模块.py
 @Software: PyCharm
 @Description:
 Python常用模块
    - 运行时服务相关模块: copy / pickle / sys / ...
    - 数学相关模块: decimal / math / random / ...
    - 字符串处理模块: codecs / re / ...
    - 文件处理相关模块: shutil / gzip / ...
    - 操作系统服务相关模块: datetime / os / time / logging / io / ...
    - 进程和线程相关模块: multiprocessing / threading / queue
    - 网络应用相关模块: ftplib / http / smtplib / urllib / ...
    - Web编程相关模块: cgi / webbrowser
    - 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...

"""
import os
import shutil
import time

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year, end=' ')
print(localtime.tm_mon, end=' ')
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(strtime)
mydate = time.strptime('2018-1-1', '%Y-%m-%d')
print(mydate)

# shutil.copy('C:/Users/asus/python.txt', 'C:/Users/asus/Desktop/first.txt')
print(os.name)
print(os.system('dir'))
# print(os.chdir('C:/Users/asus'))
os.mkdir('test')