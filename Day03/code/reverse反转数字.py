"""
 @Time    : 2022/7/15 17:11
 @Author  : Xyan9
 @File    : reverse反转数字.py
 @Software: PyCharm
 @Description:  将数字反转 如：12345 -->  54321
"""

num = int(input('num = '))
reversed_sum = 0
while num > 0:
    reversed_sum = reversed_sum * 10 + num % 10
    num //= 10
print(f'反转后的数字是{reversed_sum}')
