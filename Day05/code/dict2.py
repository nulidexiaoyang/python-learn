"""
 @Time    : 2022/7/20 9:19
 @Author  : Xyan9
 @File    : dict2.py
 @Software: PyCharm
 @Description:  字典的常用操作
"""


def main():
    stu = {'name': '许阳', 'age': 38, 'gender': True}
    print(stu)
    print(stu.keys())
    print(stu.values())
    print(stu.items())
    for elem in stu.items():
        print(elem, end=' ')
        print(elem[0], elem[1])
    if 'age' in stu:
        stu['age'] = 20
    print(stu)
    stu.setdefault('score', 60)
    print(stu)
    stu.setdefault('score', 100)
    print(stu)
    stu['score'] = 100
    print(stu)


if __name__ == '__main__':
    main()
