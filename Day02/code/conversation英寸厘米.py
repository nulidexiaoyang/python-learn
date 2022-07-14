# @Time    : 2022/7/14 22:19
# @Author  : Xyan9
# @File    : conversation英寸厘米.py
# @Software: PyCharm

value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
    print('%.4f英寸 = %.4f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.4f厘米 = %.4f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')
