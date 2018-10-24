# -*- coding: UTF-8 -*-
import socket

# AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
