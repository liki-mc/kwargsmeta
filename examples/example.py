from likiskwargsmeta import KwargsMeta

# Usage
class MyClass(metaclass = KwargsMeta):
    def __init__(self, a, b = 12):
        self.a = a
        self.b = b
    
    def method1(self, b = 3, c = 12):
        print(f"{b = }, {c = }")

MyClass(1).method1() # will print b = 12, c = 12
MyClass(12, b = 3).method1(c = 1) # will print b = 3, c = 1
MyClass(1, b = None).method1() # will print b = 3, c = 12
