class A:
    def hello(self):
        print("hello a")

    def hello_a(self):
        print("hello A")

class B:
    def hello(self):
        print("hello b")

    def hello_b(self):
        print("hello B")

class C:
    def hello(self):
        print("hello c")

    def hello_c(self):
        print("hello C")

class D(B, A, C):             #多重継承    最初はB なのでb
    def printAll(self):
        self.hello_a()
        self.hello_b()
        self.hello_c()

d = D()
d.hello_a
d.hello_b
d.hello_c
d.printAll()
d.hello()               #同じメソッドがあった場合継承の時に先に指定されたものが優先される 一番最初の"b”が出力。

