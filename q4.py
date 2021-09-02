class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # __add__
    def __add__(self, other):
        return self.a + other.a, self.b + other.b

class A:
    def __init__(self, a):
        self.a = a
    #__lt__
    def __lt__(self, other):
        if (self.a < other.a):
            return "object1 is less than object 2"
        else:
            return "object2 is less than object1"
    #__eq__
    def __eq__(self, other):
        if (self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"


Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)

ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print(ob1 == ob2)