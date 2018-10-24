# -*- coding: UTF-8-*-
from enum import Enum, unique

# 该注解可以保证枚举类型唯一
@unique
class Month(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


if __name__ == '__main__':
    Exception
    for month in Month:
        print(month)
