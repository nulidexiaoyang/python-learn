"""
 @Time    : 2022/7/23 17:02
 @Author  : Xyan9
 @File    : diamond菱形继承.py
 @Software: PyCharm
 @Description:
    多重继承
    - 菱形继承(钻石继承)
    - C3算法(替代DFS的算法)
"""


class A(object):

    def foo(self):
        print('foo of A')


class B(A):

    pass
    # def foo(self):
    #     print('foo fo B')


class C(A):

    def foo(self):
        print('foo fo C')


class D(B, C):

    # pass的话先找B的foo，再找C的foo
    pass
    # def foo(self):
    #     print('foo fo D')


class E(D):

    def foo(self):
        print('foo in E')
        super().foo()
        super(B, self).foo()
        super(C, self).foo()


def main():
    d = D()
    d.foo()
    e = E()
    e.foo()


if __name__ == '__main__':
    main()
