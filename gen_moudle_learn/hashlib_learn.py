# -*- coding: utf-8 -*-
import hashlib

# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
if __name__ == '__main__':
    md5 = hashlib.md5()
    md5 = hashlib.md5()
    md5.update('how to use md5 in '.encode('utf-8'))
    md5.update('python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())

    sha1 = hashlib.sha1()
    sha1.update('what the fuck'.encode('utf-8'))
    print(sha1.hexdigest())