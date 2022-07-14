# @Time    : 2022/7/13 17:24
# @Author  : Xyan9
# @File    : circle计算圆.py
# @Software: PyCharm
import math

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print(f'周长：{perimeter:.2f}')
print('面积：%.2f' % area)
