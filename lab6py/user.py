from data import defaultroundto
from data import memory

class User:
    def __init__(self,name):
        self.name = name
        self.roundto = defaultroundto
        self.memory = memory