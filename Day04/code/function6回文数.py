"""
 @Time    : 2022/7/18 10:09
 @Author  : Xyan9
 @File    : function6回文数.py
 @Software: PyCharm
 @Description: 12321是回文数
"""


def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


if __name__ == '__main__':
    print(121)
