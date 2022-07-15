"""
 @Time    : 2022/7/15 21:58
 @Author  : Xyan9
 @File    : prime素数.py
 @Software: PyCharm
 @Description:  输出2~99之间的素数
"""
import math

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
