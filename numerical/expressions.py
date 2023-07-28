from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def has_variable(self):
        pass

    @abstractmethod
    def evaluate(self, **variables):
        pass


class Constant(Expression):
    def __init__(self, value):
        pass

    def has_variable(self):
        pass

    def evaluate(self, **variables):
        pass


class Variable(Expression):
    def __init__(self, name):
        pass

    def has_variable(self):
        pass

    def evaluate(self, **variables):
        pass
