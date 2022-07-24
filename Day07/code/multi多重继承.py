"""
 @Time    : 2022/7/23 16:55
 @Author  : Xyan9
 @File    : multi多重继承.py
 @Software: PyCharm
 @Description:
     多重继承
    - 通过多重继承可以给一个类的对象具备多方面的能力
    - 这样在设计类的时候可以避免设计太多层次的复杂的继承关系
"""


class Father(object):

    def __init__(self, name):
        self._name = name

    def gamble(self):
        print(f'{self._name}在打麻将')

    def eat(self):
        print('%s在大吃大喝.' % self._name)


class Monk(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%s在吃斋.' % self._name)

    def chant(self):
        print('%s在念经.' % self._name)


class Musician(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%s在细嚼慢咽.' % self._name)

    def play_piano(self):
        print('%s在弹钢琴.' % self._name)


# 试一试下面的代码看看有什么区别
# class Son(Monk, Father, Musician):  # 继承了Monk的eat的方法
# class Son(Musician, Father, Monk):  #  继承了Musician的eat方法
class Son(Father, Monk, Musician):   # 继承了Musician的eat方法

    def __init__(self, name):
        Father.__init__(self, name)
        Monk.__init__(self, name)
        Musician.__init__(self, name)


def main():
    son = Son('王大锤')
    son.gamble()
    # 调用继承自Father的eat方法
    son.eat()
    son.chant()
    son.play_piano()


if __name__ == '__main__':
    main()
