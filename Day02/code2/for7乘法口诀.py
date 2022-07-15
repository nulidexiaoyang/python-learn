"""
 @Time    : 2022/7/15 17:05
 @Author  : Xyan9
 @File    : for7乘法口诀.py
 @Software: PyCharm
 @Description:  打印乘法口诀表
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (j, i, i * j), end='\t')
    print()
