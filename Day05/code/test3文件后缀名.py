"""
 @Time    : 2022/7/20 10:00
 @Author  : Xyan9
 @File    : test3文件后缀名.py
 @Software: PyCharm
 @Description:  文件后缀名
"""


def get_suffix(filename, has_dot=False):
    """
    获取文件的后缀名
    :param filename: 文件名
    :param has_dot:  返回的后缀名是否需要带'.'
    :return: 文件后后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


def main():
    last_name = get_suffix('test1屏幕跑马灯.py', True)
    print(last_name)


if __name__ == '__main__':
    main()
