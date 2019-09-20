#!/usr/bin/python3
# coding: utf-8


class ClassicInt(int):
    def __init__(self, integer):
        assert isinstance(integer, int),(
                'Expected a `int` value.'
                f' But got {type(integer).__name__}'
                )
        self.integer = integer
        self.numbers = [int(i) for i in str(integer)]
        self.__class__.__call__ = self.integer

    def __repr__(self):
        return f'{self.integer}'

    def __len__(self):
        return len(self.numbers)

    def __iter__(self):
        for number in self.numbers:
            yield number

    def __add__(self, others=None):
        if not others:
            return sum(self.numbers)
        return self.integer + others
    
    def __sum__(self, others=None):
        if not others:
            return sum(self.numbers)
        return self.numbers + others
    
    def __getitem__(self, index):
        return self.numbers[index]

    def __bool__(self):
        return bool(abs(self))
    
    def __reversed__(self):
        return reversed(self.numbers)
    
    def as_list(self):
        return self.numbers
    
    def index(self, value):
        return self.numbers.index(value)