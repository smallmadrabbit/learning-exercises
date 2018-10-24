#  -*- coding:UTF-8 -*-
import json


class Holder(object):
    def __init__(self, name, age, no):
        self.name = name
        self.age = age
        self.no = no


if __name__ == '__main__':
    b = Holder('zhangsan', 11, 11)
    print(json.dumps(b, default=lambda obj: obj.__dict__))
