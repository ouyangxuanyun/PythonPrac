"""
7-3 实现对象上下文管理
"""

from sys import stdin, stdout
import getpass
import telnetlib
from collections import deque


class TelnetClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __enter__(self):
        self.tn = telnetlib.Telnet(self.host, self.port)
        self.history = deque([])

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tn.close()
        self.tn = None

        with open('history.txt', 'a') as f:
            f.writelines(self.history)

    def login(self):
        pass
