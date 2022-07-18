"""
 @Time    : 2022/7/18 10:10
 @Author  : Xyan9
 @File    : function7回文素数.py
 @Software: PyCharm
 @Description:  引用function2和function6
"""

from function6回文数 import is_palindrome
from function8素数 import is_prime

if __name__ == '__main__':
    num = int(input('请输入正整数：'))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)
    else:
        print(f'{num}不是回文素数')
