"""
 @Time    : 2022/7/18 10:13
 @Author  : Xyan9
 @File    : function8素数.py
 @Software: PyCharm
 @Description:  素数
"""


def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    if num != 1:
        return True
    else:
        return False
