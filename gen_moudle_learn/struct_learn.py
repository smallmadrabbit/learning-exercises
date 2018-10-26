# -*- coding: utf-8 -*-
import struct

# Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str
# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换

if __name__ == '__main__':
    url = 'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000' \
          '/001431955007656a66f831e208e4c189b8a9e9f3f25ba53000'
    print('感觉不是很常用啊，直接去网址看吧', url)
