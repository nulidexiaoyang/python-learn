"""
 @Time    : 2022/7/20 10:11
 @Author  : Xyan9
 @File    : test4列表中最大和第二大的元素的值.py
 @Software: PyCharm
 @Description:  列表中最大和第二大的元素的值
"""


def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


def main():
    list1 = [1, 3, 45, 43, 12, 345]
    list2 = max2(list1)
    print(list2)


if __name__ == '__main__':
    main()
