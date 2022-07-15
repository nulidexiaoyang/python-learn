# @Time    : 2022/7/15 9:11
# @Author  : Xyan9
# @File    : for4素数判断.py
# @Software: PyCharm
# @Description:  输入一个数判断是不是素数
import math

num = int(input('请输入一个数字：'))
end = int(math.sqrt(num))
is_prime = True
for x in range(2, end+1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')

