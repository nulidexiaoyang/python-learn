"""
 @Time    : 2022/7/20 9:23
 @Author  : Xyan9
 @File    : test1屏幕跑马灯.py
 @Software: PyCharm
 @Description:  屏幕跑马灯
"""
import os
import time


def main():
    content = '河南大学欢迎您......'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(1)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
