"""
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

num = int(input('请输入一个正整数: '))
temp = num
num2 = 0
#新建一个数，把输入的数反过来，再判断是否相等
while temp > 0:
    num2 *= 10
    num2 += temp % 10
    temp //= 10
if num == num2:
    print('%d是回文数' % num)
else:
    print('%d不是回文数' % num)

#回文数也可以用下面方法判断
# if num == int(str(num)[::-1]):
#     print('%d是回文数' % num)
# else:
#     print('%d不是回文数' % num)