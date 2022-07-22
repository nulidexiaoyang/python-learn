"""
 @Time    : 2022/7/22 8:50
 @Author  : Xyan9
 @File    : circle泳池.py
 @Software: PyCharm
 @Description:
     修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
    过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
    输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)
"""
import math


class Circle(object):

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return  self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @property
    def perimeter(self):
        return math.pi * self._radius * 2

    @property
    def area(self):
        return math.pi * self._radius * self._radius


def main():
    radius = float(input('请输入游泳池的半径'))
    small = Circle(radius)
    big = Circle(radius + 3)
    print(f'围墙造价为：￥{(big.perimeter * 115):.1f}元')
    print(f'过道造价为：￥{((big.area - small.area) * 65):.1f}元')


if __name__ == '__main__':
    main()
