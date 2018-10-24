#  -*- coding:UTF-8 -*-
from abc import abstractmethod, ABCMeta
from io import StringIO, BytesIO


class TestInterface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_name(self):
        pass


class TestProject(TestInterface):
    def something(self):
        print('something')


if __name__ == '__main__':
    f = StringIO()
    f.write('zhangsan')
    fb = BytesIO()
    fb.write('雷猴'.encode('utf-8'))
    print('str'.endswith('r'))
    print('str'.startswith('s'))
    print('ssssssstrsssss'.count('s'))
    print('sss'.upper())

