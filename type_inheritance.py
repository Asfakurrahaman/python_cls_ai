class A:
    def display1(self):
        print("A")

class B:
    def display2(self):
        print("B")


class C:
    def display3(self):
        print("C")

class D(A,B,C):
    pass

ob1 = D()
ob1.display3()
ob1.display2()
ob1.display1()