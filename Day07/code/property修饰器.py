"""
 @Time    : 2022/7/22 16:19
 @Author  : Xyan9
 @File    : property修饰器.py
 @Software: PyCharm
 @Description:
     property修饰器
     访问器
     修改器
"""


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print(f'{self._name}正在玩飞行器')
        else:
            print(f'{self._name}正在玩斗地主')


def main():
    person = Person('王大锤', 21)
    person.play()
    person.age = 14
    person.play()


if __name__ == '__main__':
    main()
