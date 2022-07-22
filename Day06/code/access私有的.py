"""
 @Time    : 2022/7/21 17:11
 @Author  : Xyan9
 @File    : access私有的.py
 @Software: PyCharm
 @Description:
"""


class Test:

    def __init__(self, foo):
        # 私有属性
        self.__foo = foo

    def __bar(self):
        # 私有方法
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # 通过_来访问私有属性和方法
    test._Test__bar()
    print(test._Test__foo)


if __name__ == '__main__':
    main()
