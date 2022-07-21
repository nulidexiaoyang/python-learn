"""
 @Time    : 2022/7/19 17:31
 @Author  : Xyan9
 @File    : tuple1.py
 @Software: PyCharm
 @Description:
    元组的定义和使用
"""


def main():
    # 定义元组
    t = ('许阳', 38, True, '河南开封')
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[1])
    print(t[2])
    print(t[3])
    # 遍历元组中的值
    for member in t:
        print(member)
    # 重新给元组赋值
    # t[0] = '王大锤  # TypeError
    # 变量t重新应用了新的元组 原来的元组被垃圾回收
    t = ('王大锤', 20, True, '中国台湾')
    print(t)
    # 元组和列表的转换
    person = list(t)
    print(person)
    person[0] = '马云'
    person[1] = 25
    print(person)
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)


if __name__ == '__main__':
    main()