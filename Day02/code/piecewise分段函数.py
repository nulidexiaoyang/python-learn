# @Time    : 2022/7/14 16:53
# @Author  : Xyan9
# @File    : piecewise分段函数.py
# @Software: PyCharm

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'f({x:.2f}) = {y:.2f}')
