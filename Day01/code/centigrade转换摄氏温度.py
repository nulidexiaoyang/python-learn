# @Time    : 2022/7/13 17:23
# @Author  : Xyan9
# @File    : centigrade转换摄氏温度.py
# @Software: PyCharm

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
