"""
 @Time    : 2022/7/21 16:50
 @Author  : Xyan9
 @File    : student.py
 @Software: PyCharm
 @Description: 学生类
"""


class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age, sex='男'):
        self.name = name
        self.age = age
        # sex是私有的属性
        self.__sex = sex

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print(f'{self.name}只能观看《儿童动画》')
        else:
            print(f'{self.name}正在观看岛国爱情大电影')

    # 私有的方法
    def __display_sex(self):
        print(self.__sex)

    def use_sex(self):
        self.__display_sex()


def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('小羊', 23)
    # 给对象发study消息
    stu1.study('《Python程序设计》')
    stu2 = Student('李元芳', 45)
    stu2.study('思想')
    stu2.watch_movie()
    stu1.use_sex()


if __name__ == '__main__':
    main()
