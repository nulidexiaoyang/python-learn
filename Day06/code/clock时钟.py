"""
 @Time    : 2022/7/21 17:16
 @Author  : Xyan9
 @File    : clock时钟.py
 @Software: PyCharm
 @Description:  数字时钟
"""
from time import sleep


class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化方法
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return f'{self._hour:02d}:{self._minute:02d}:{self._second:02d}'


def main():
    clock1 = Clock(23, 59, 58)
    while True:
        print(clock1.show())
        sleep(1)
        clock1.run()


if __name__ == '__main__':
    main()
