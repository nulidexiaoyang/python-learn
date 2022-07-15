# @Time    : 2022/7/15 9:21
# @Author  : Xyan9
# @File    : for6打印三角形.py
# @Software: PyCharm
# @Description:  打印三种三角形

row = int(input('请输入行数：'))
for i in range(row):
    for j in range(i + 1):
        print('*', end='')
    # end默认换行 print(self, *args, sep=' ', end='\n', file=None)
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()
