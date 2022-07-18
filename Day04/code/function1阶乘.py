"""
 @Time    : 2022/7/17 16:34
 @Author  : Xyan9
 @File    : function1阶乘.py
 @Software: PyCharm
 @Description:  封装一个函数求阶乘
"""


def factorail(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


print(factorail(7) // factorail(3))
