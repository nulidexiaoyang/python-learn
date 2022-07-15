"""
 @Time    : 2022/7/15 21:54
 @Author  : Xyan9
 @File    : fibonacci斐波那契.py
 @Software: PyCharm
 @Description:      输出斐波那契数列的前20个数
                    1 1 2 3 5 8 13 21 ...
"""
a = 0
b = 1
for i in range(20):
    a, b = b, a + b
    print(a, end=' ')
