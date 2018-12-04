
class User:
    def _init_(self, name):
        self.name = name
    def hello(self):
        print("hello " + self.name)

#継承
class SuperUser(User):                        
    def _init_(self, name, age):
        super()._init_(name)
        self.age = age

# オーバーライドして親クラスに上書きしている。
    def hello(self):   

        super().hello()                             #親クラスのhelloを呼び出したい場合。               
       # print("SuperUser hello " + self.name )
    
super_aitv_ = SuperUser("aitv ", 8) 
super_aitv_.hello()

