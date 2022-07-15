# @Time    : 2022/7/15 9:14
# @Author  : Xyan9
# @File    : for5公约数和公倍数.py
# @Software: PyCharm
# @Description: 计算两个数字的最大公约数 和 最小公倍数

x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
