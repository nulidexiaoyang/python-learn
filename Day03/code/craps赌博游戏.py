"""
 @Time    : 2022/7/15 21:42
 @Author  : Xyan9
 @File    : craps赌博游戏.py
 @Software: PyCharm
 @Description:      玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
                    如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
                    玩家再次要色子 如果摇出7点 庄家胜
                    如果摇出第一次摇的点数 玩家胜
                    否则游戏继续 玩家继续摇色子
                    玩家进入游戏时有1000元的赌注 全部输光游戏结束
"""
from random import randint

money = 1000
while money > 0:
    print(f'你的总资产为：{money}')
    needs_go_on = False
    while True:
        debt = int(input('下注：'))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print(f'玩家骰出了{first}点')
    if first == 7 or first == 11:
        print('玩家胜！')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print(f'玩家骰出了{current}点')
        if current == 7:
            print('庄家胜!')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜!')
            money += debt
            needs_go_on = False
print('你破产了，游戏结束！')
