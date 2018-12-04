
class SampleClass:
    pass            #空のクラスを作る場合パスと書く
sample = SampleClass()              #クラス名＋（）でインスタンス化する事ができる
sample2 = SampleClass()

sample.name = "A"
sample2.name = "B"

print(sample.name)
print(sample2.name)