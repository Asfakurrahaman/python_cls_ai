class A:
    def display1(self):
        print("A")

class B(A):
    def display2(self):
        print("B")


class C(B):
    def display3(self):
        print("C")
        pass

ob1 = C()
ob1.display3()
ob1.display2()
ob1.display1()