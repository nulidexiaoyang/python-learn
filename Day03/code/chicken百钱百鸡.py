"""
 @Time    : 2022/7/15 17:13
 @Author  : Xyan9
 @File    : chicken百钱百鸡.py
 @Software: PyCharm
 @Description:  百钱百鸡问题：公鸡5元一只，母鸡3元一只，小鸡1元三只，
                用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print(f'公鸡：{x}只  母鸡：{y}只  小鸡：{z}只')
