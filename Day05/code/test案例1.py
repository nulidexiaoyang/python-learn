"""
 @Time    : 2022/7/20 16:49
 @Author  : Xyan9
 @File    : test案例1.py
 @Software: PyCharm
 @Description:
"""
import random


def display(balls):
    """
    输出列表中的双色球号码
    :param balls: 双色球号码
    :return: 无返回值
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print(f'{ball:02d}', end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    :return: 返回值为一组号码
    """
    red_balls = [x for x in range(1, 34)]
    select_balls = []
    select_balls = random.sample(red_balls, 6)
    select_balls.sort()
    select_balls.append(random.randint(1, 16))
    return select_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()

