# -*- coding: utf-8 -*-
import base64

if __name__ == '__main__':
    print(base64.b64encode(b'params?=helloworld,woca'))
    decode = base64.b64decode(b'cGFyYW1zPz1oZWxsb3dvcmxkLHdvY2E=')
    print(type(decode), decode)
    bytes_decode = bytes.decode(decode)
    print(type(bytes_decode), bytes_decode)

    # bytes object
    b = b"example"
    # str object
    s = "example"
    # str to bytes
    bytes(s, encoding="utf8")
    # bytes to str
    str(b, encoding="utf-8")
    # an alternative method
    # str to bytes
    str.encode(s)
    # bytes to str
    bytes.decode(b)
