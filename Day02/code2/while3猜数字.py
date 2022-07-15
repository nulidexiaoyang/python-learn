"""
 @Time    : 2022/7/15 17:01
 @Author  : Xyan9
 @File    : while3猜数字.py
 @Software: PyCharm
 @Description:  计算机出一个1~100之间的随机数由人来猜
                计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('猜对了')
        break
print('你一共猜了%d次' % counter)
if counter > 7:
    print('你的智商不行啊')
