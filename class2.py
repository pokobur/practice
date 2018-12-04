class Person:
    name = ("キノ")
    age = ("(21)")
    sex = (",男性")
    
    def prf(self):
        print(self.sex)
        print("血液型: O型", end="")
        print("\n職業：プログラマー")
        print("そして神である。")
    
obj = Person()    #クラスのインスタンス生成（オブジェクト変数）これによりクラスを呼び出している

print(obj.name,end="")    #オブジェクト変数がクラスの内容を呼び出している
print(obj.age,end="")
obj.prf()    #オブジェクト変数がクラス内のメソッドを呼び出している

