# @Time    : 2022/7/13 17:33
# @Author  : Xyan9
# @File    : strings字符串.py
# @Software: PyCharm

str1 = 'hello, world!'
print('字符串的长度是:', len(str1))
print('单词首字母大写: ', str1.title())
print('字符串变大写: ', str1.upper())
# str1 = str1.upper()
print('字符串是不是大写: ', str1.isupper())
print('字符串是不是以hello开头: ', str1.startswith('hello'))
print('字符串是不是以hello结尾: ', str1.endswith('hello'))
print('字符串是不是以感叹号开头: ', str1.startswith('!'))
print('字符串是不是一感叹号结尾: ', str1.endswith('!'))

# 十进制 35768 和 38451
str2 = '- \u8BB8\u9633'
str3 = str1.title() + ' ' + str2.lower()
print(str3)
