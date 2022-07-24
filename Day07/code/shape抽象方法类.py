"""
 @Time    : 2022/7/22 17:16
 @Author  : Xyan9
 @File    : shape抽象方法类.py
 @Software: PyCharm
 @Description:
     继承的应用
    - 抽象类
    - 抽象方法
    - 方法重写
    - 多态
"""
import math
from abc import ABCMeta, abstractmethod


class Shape(object, metaclass=ABCMeta):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def perimeter(self):
        return 2 * math.pi * self._radius

    def area(self):
        return math.pi * self._radius ** 2

    def __str__(self):
        return '我是一个圆'


class Rect(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __str__(self):
        return '我是一个矩形'


def main():
    shapes = [Circle(5), Circle(3.2), Rect(3.2, 6.3)]
    for shape in shapes:
        print(shape)
        print('周长:', shape.perimeter())
        print('面积:', shape.area())


if __name__ == '__main__':
    main()
