"""Класс лотерейный билет"""
from random import randint, choice

class Lottery():
    def __init__(self):
        self.range = ('1234567890abcd',)
    def get_chance(self, let_replayses=False):
        ret = ''
        while len(ret)<4:
            sym = choice(self.range[0])
            if let_replayses or not sym in ret:
                ret += sym
        return ret