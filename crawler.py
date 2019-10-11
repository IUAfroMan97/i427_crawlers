import os

class Crawler(object):
    def __init__(self, name):
        self.name = name
        self.ppid = os.getppid()

    def setPid(self, pid):
        self.pid = pid

    
    