"""
 @Time    : 2022/7/20 10:23
 @Author  : Xyan9
 @File    : test6杨辉三角.py
 @Software: PyCharm
 @Description:  打印杨辉三角
"""
import random


def main():
    num = 4
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()
    random.sample
