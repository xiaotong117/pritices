"""
输出2~99之间的素数

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
















import math

for num in range(2, 100):
    is_prime = True
    #这里的范围用num开根号向上取整数，可以缩短循环范围
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            #判断为非素数后立即跳出，避免不必要的资源浪费
            break
    if is_prime:
        print(num, end=' ')
