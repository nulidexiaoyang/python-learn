"""
 @Time    : 2022/7/18 10:23
 @Author  : Xyan9
 @File    : function9.py
 @Software: PyCharm
 @Description:  作用域
"""


# 局部作用域
def foo1():
    a = 5


foo1()
# print(a)  # NameError

# 全局作用域
b = 10


def foo2():
    print(b)


foo2()


def foo3():
    b = 100     # 局部变量
    print(b)


foo3()
print(b)


def foo4():
    global b
    b = 200     # 全局变量
    print(b)


foo4()
print(b)

