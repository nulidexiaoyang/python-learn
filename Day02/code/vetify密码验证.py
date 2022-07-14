# @Time    : 2022/7/14 16:58
# @Author  : Xyan9
# @File    : vetify密码验证.py
# @Software: PyCharm
import getpass

username = input('请输入用户名：')
password = input('请输入密码：')
if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')