# @Time    : 2022/7/15 9:09
# @Author  : Xyan9
# @File    : for3阶乘.py
# @Software: PyCharm
# @Description:  输入整数n，计算n的阶乘n!

n = int(input('n = '))
result = 1
for x in range(1, n+1):
    result *= x
print(f'{n}! = {result}')
