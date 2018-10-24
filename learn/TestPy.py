#  -*- coding:UTF-8 -*-
import sys
import logging


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("test")
    f = open('test', 'a', encoding='gbk')
    f.write('\n')
    f.close()
