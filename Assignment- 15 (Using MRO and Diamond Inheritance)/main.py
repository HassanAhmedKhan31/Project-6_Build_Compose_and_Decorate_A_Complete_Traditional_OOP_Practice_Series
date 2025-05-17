class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# Example
d = D()
d.show()  # Output: B
print(D.__mro__)  # Show method resolution order
