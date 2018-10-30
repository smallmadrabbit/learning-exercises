# -*- coding: utf-8 -*-
import itertools


def count_iter():
    # 无限迭代器1, 加
    natuals = itertools.count(1)
    for n in natuals:
        print(n)


def cycle_iter():
    # 无限迭代器，循环
    cycle = itertools.cycle('ABCD')
    for c in cycle:
        print(c)


def repeat_iter():
    # 无限迭代器，重复，第二个参数指定循环次数
    repeat = itertools.repeat('gf', 5)
    for t in repeat:
        print(t)


def chain_iter():
    # 将一组迭代对象串联，组成一个更大的迭代器
    chain = itertools.chain('ABC', 'XYZ')
    for t in chain:
        print(t)


def group_by():
    # 将可迭代的对象中重复的元素提取出来放在一组
    str = 'AADSDASDASDECCSADQWWQQDAADASSSADAAVV'
    group = itertools.groupby(str)
    for key, value in group:
        print(type(key), type(value))
        print(key, list(value))


def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd_iter = itertools.count(1, 2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    pn_repeat_iter = itertools.cycle([4, -4])
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    sum = 0.0
    for i in range(N):
        base = odd_iter.__next__()
        z = pn_repeat_iter.__next__()
        sum += z / base

    # step 4: 求和:
    return sum


if __name__ == '__main__':
    # count_iter()
    # cycle_iter()
    # repeat_iter()
    # chain_iter()
    # group_by()

    # 求圆周率
    print(pi(999999999))
