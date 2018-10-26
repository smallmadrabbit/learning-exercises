#  -*- coding:UTF-8 -*-
import json


class Holder(object):
    def __init__(self, name, age, no):
        self.name = name
        self.age = age
        self.no = no


def dump_method(obj):
    return obj.__dict__


if __name__ == '__main__':
    b = Holder('zhangsan', 11, 11)
    # 方法一 与 方法二 等效
    # method: 1
    print(json.dumps(b, default=dump_method(b)))
    # method: 2
    print(json.dumps(b, default=lambda obj: obj.__dict__))
