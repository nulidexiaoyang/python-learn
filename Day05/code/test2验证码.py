"""
 @Time    : 2022/7/20 9:53
 @Author  : Xyan9
 @File    : test2验证码.py
 @Software: PyCharm
 @Description:  验证码
"""
import random


def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度
    :return: 大小写字幕和数字构成的 随机验证码
    """
    all_chars = '0123456789qwertyuiopasdfghjklzxcvbnm'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def main():
    code = generate_code()
    print(code)


if __name__ == '__main__':
    main()
