# -*- coding: utf-8 -*-
from contextlib import contextmanager


class Query(object):
    # 较为繁琐的写法
    def __init__(self, name):
        self.name = name

    # 上线文管理通过__enter__ 和__exit__ 两个函数实现
    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info is %s...' % self.name)


class SimpleQuery(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('simple query name is %s ...' % self.name)


# 在某一段代码前后执行指定代码，类似java中的装饰器,代理模式
@contextmanager
def create_query(name):
    print('begin')
    q = SimpleQuery(name)
    yield q
    print('end')


if __name__ == '__main__':
    with create_query('Bob') as q:
        q.query()
        q.query()
