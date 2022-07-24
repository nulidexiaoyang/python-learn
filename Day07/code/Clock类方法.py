"""
 @Time    : 2022/7/22 16:53
 @Author  : Xyan9
 @File    : Clock类方法.py
 @Software: PyCharm
 @Description:  类方法的应用
"""
from time import localtime, time, sleep


class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    # 类方法 cls，它代表的是当前类相关的信息的对象
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
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
        return f'{self._hour:02d}:{self._minute:02d}:{self._second:02d}'


def main():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
