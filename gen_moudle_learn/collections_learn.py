# -*- coding: utf-8 -*-
from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter


def namedtuple_learn():
    # 问题： tuple可以标识不变集合，例如(x, y)可以表示一个坐标，但是定义一个类过于繁琐
    # 所以使用namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x)
    print(p.y)


def deque_learn():
    # 使用list按照索引访问数据很快，但是插入删除很慢
    # deque实现插入和删除操作的双向列表
    # 适用于队列和栈
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')
    print(q)
    print(q.pop(), q)


def defaultdict_learn():
    # dict使用时如果不存在则会返回一个KeyError异常
    # 如果想要返回一个默认值，则可以使用defaultdict
    dd = defaultdict(lambda: 'N/A')
    dd['name'] = 'value'
    print(dd['key'])
    print(dd['name'])


def ordereddict_learn():
    # 默认字典是按照key排序的
    # OrderedDict是按照插入顺序排序的
    # 搜索
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(od)


# FIFO_DICT
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


def chainmap_learn():
    # ChainMap可以把一组dict串起来并组成一个逻辑上的dict。
    # ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
    cm = ChainMap({'name': 'john', 'age': 20}, {'mobile': '17600104924'})
    print(cm)
    print(cm['name'])
    print(cm['mobile'])


def count_learn():
    names = ['john', 'siri', 'air', 'dick', 'dick', 'fuck', 'what']
    c = Counter()
    for name in names:
        c[name] += 1
    print(type(c), c)
    print(type(c.values()), c.values())


if __name__ == '__main__':
    # namedtuple_learn()
    # deque_learn()
    # defaultdict_learn()
    # orderedDict_learn()
    # chainmap_learn()
    # count_learn()
    pass
