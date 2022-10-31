#Access parent class with single inheritance
class A:
    def f1(self):
        print("This is classs A")
    #parent class is also known as super class or base class
class B(A):
    def f2(self):
        print("This is class B")
    #child class is also known as derived class or sub class
a=A()
b=B()
a.f1()
b.f2()
b.f1()
