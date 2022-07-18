"""
 @Time    : 2022/7/17 17:15
 @Author  : Xyan9
 @File    : function5函数参数.py
 @Software: PyCharm
 @Description:
    函数的参数
    - 位置参数
    - 可变参数
    - 关键字参数
    - 命名关键字参数
"""


# 参数默认值
def f1(a, b=5, c=10):
    return a + b * 2 + c * 3


print(f1(1, 2, 3))
print(f1(100, 200))
print(f1(100))
print(f1(c=2, b=3, a=1))  # 3 + 6 + 2


# 可变参数
def f2(*args):
    sum_ = 0
    for num in args:
        sum_ += num
    return sum_


print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())


# 关键字参数
def f3(**kw):
    if 'name' in kw:
        print('欢迎你%s!' % kw['name'])
    elif 'tel' in kw:
        print('你的联系电话是: %s!' % kw['tel'])
    else:
        print('没找到你的个人信息!')


param = {'name': '许阳', 'age': 38}
f3(**param)
f3(name='许阳', age=38, tel='11333333')
f3(user='许阳', age=38, tel='11333333')
f3(user='许阳', age=38, mobile='11333333')
