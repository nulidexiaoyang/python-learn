"""
 @Time    : 2022/7/15 17:08
 @Author  : Xyan9
 @File    : lily水仙花.py
 @Software: PyCharm
 @Description:  寻找100~999水仙花数
"""

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(f'{num}')
