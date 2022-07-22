"""
 @Time    : 2022/7/22 9:06
 @Author  : Xyan9
 @File    : rect矩形.py
 @Software: PyCharm
 @Description:
 定义和使用矩形类
"""


class Rect(object):

    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def perimeter(self):
        return (self._width + self._height) * 2

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return '矩形[%f,%f]' % (self._width, self._height)

    def __del__(self):
        print('销毁矩形对象')


def main():
    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter)
    print(rect1.area)
    rect2 = Rect(3.5, 4.5)
    print(rect2)


if __name__ == '__main__':
    main()
