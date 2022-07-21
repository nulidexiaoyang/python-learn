"""
 @Time    : 2022/7/20 9:00
 @Author  : Xyan9
 @File    : dict1.py
 @Software: PyCharm
 @Description:  定义和使用字典
"""


def main():
    scores = {'许阳': 95, '白元芳': 78, '狄仁杰': 70}
    print(scores['许阳'])
    print(scores['狄仁杰'])
    for elem in scores:
        print(f'{elem}--->{scores[elem]}\t')
    scores['白元芳'] = 65
    scores['诸葛王朝'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    print(scores.get('武则天', 60))
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('许阳', 100))
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()
