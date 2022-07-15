"""
 @Time    : 2022/7/15 9:35
 @Author  : Xyan9
 @File    : while2偶数求和.py
 @Software: PyCharm
 @Description:  偶数求和
"""

sum_, num = 0, 2
while num <= 100:
    sum_ += num
    num += 2
print(sum_)