import sys
import ctypes

class Pointer:
    def __init__(self, var: any):
        self.pointsToVal = var
        self.pointsToAddress = id(self.pointsToVal)

    def getAddress(self):
        return self.pointsToAddress

    def getVal(self):
        return self.pointsToVal

    def increment(self):
        self.pointsToAddress += sys.getsizeof(self.pointsToVal)
        self.pointsToVal = ctypes.cast(self.pointsToAddress, ctypes.py_object).value

    def decrement(self):
        self.pointsToAddress -= sys.getsizeof(self.pointsToVal)
        self.pointsToVal = ctypes.cast(self.pointsToAddress, ctypes.py_object).value

    def add(self, val: int):
        self.pointsToAddress += val * sys.getsizeof(self.pointsToVal)
        self.pointsToVal = ctypes.cast(self.pointsToAddress, ctypes.py_object).value

    def sub(self, val: int):
        self.pointsToAddress -= val * sys.getsizeof(self.pointsToVal)
        self.pointsToVal = ctypes.cast(self.pointsToAddress, ctypes.py_object).value

    def eqeq(self, other):
        return self.pointsToAddress == other.pointsToAddress
    
    def ne(self, other):
        return self.pointsToAddress != other.pointsToAddress

    def gt(self, other):
        return self.pointsToAddress > other.pointsToAddress

    def lt(self, other):
        return self.pointsToAddress < other.pointsToAddress

    def lte(self, other):
        return self.pointsToAddress <= other.pointsToAddress

    def gte(self, other):
        return self.pointsToAddress >= other.pointsToAddress