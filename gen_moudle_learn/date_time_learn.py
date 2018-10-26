# -*- coding: UTF-8 -*-
from datetime import datetime

if __name__ == '__main__':
    d = datetime.now()
    print('year is %d' % d.year)
    print('month is %d' % d.month)
    print('day is %d' % d.day)
    print('date is %s' % d.date())

    timestamp = d.timestamp()
    print(datetime.fromtimestamp(timestamp))

    print(datetime.strptime('2018-11-11 23:11:11', '%Y-%m-%d %H:%M:%S'))