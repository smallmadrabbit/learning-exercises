# -*- coding: UTF-8 -*-
class KWObject(object):
    @classmethod
    def print_kw_args(cls, *args, **kwargs):
        print('*args is', args)
        print('**kwargs is', kwargs)


if __name__ == '__main__':
    KWObject.print_kw_args(1, 2, 3, 4)
    KWObject.print_kw_args(name='zhangsan', age='15')
    KWObject.print_kw_args(1, 2, 3, name='lisi', age='20')
