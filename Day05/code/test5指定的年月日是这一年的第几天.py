"""
 @Time    : 2022/7/20 10:14
 @Author  : Xyan9
 @File    : test5指定的年月日是这一年的第几天.py
 @Software: PyCharm
 @Description:  指定的年月日是这一年的第几天
"""


def is_leap_year(year):
    """
    判断指定的年份是不是闰年
    :param year: 年份
    :return: 闰年返回True
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, day):
    """
    计算传入的日期是这一年的第几天
    :param year: 年
    :param month: 月
    :param day: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + day


def main():
    day = which_day(2000, 10, 3)
    print(day)


if __name__ == '__main__':
    main()
