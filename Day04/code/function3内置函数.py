"""
 @Time    : 2022/7/17 16:39
 @Author  : Xyan9
 @File    : function3内置函数.py
 @Software: PyCharm
 @Description:
    Python的内置函数
    - 数学相关: abs / divmod / pow / round / min / max / sum
    - 序列相关: len / range / next / filter / map / sorted / slice / reversed
    - 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
    - 数据结构: dict / list / set / tuple
    - 其他函数: all / any / id / input / open / print / type

"""


def myfilter(mystr):
    return len(mystr) == 6


# help()
print(chr(0x8BB8))
print(hex(ord('阳')))
print(abs(-1.2345))
print(round(1.2345))
print(pow(3, 5))
fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1, 3)])
fruits2 = list(filter(myfilter, fruits)) # 筛选出长度为6的字符串
print(fruits)
print(fruits2)

