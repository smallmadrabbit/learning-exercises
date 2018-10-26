# -*- coding: utf-8 -*-
import hmac

# 加盐的hash，或理解为使用指定Key来生成hash值
if __name__ == '__main__':
    message = b'my friend'
    key = b'wtf'
    h = hmac.new(key, message, digestmod='MD5')
    print(type(h.hexdigest()), h.hexdigest())
