"""
 @Time    : 2022/7/21 17:14
 @Author  : Xyan9
 @File    : student2另一种定义类.py
 @Software: PyCharm
 @Description:  另一种定义类的方法
"""


def bar(self, name):
    self._name = name


def foo(self, course_name):
    print(f'{self._name}正在学习{course_name}')


def main():
    Student1 = type('Student1', (object,), dict(__init__=bar, study=foo))
    stu1 = Student1('小羊')
    stu1.study('Python程序设计')


if __name__ == '__main__':
    main()
