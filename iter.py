#iter() next() イテレータについて
#イテレータはリストから文字列を取り出すしくみ

nums = [5,8,11]
i = iter(nums)
print(next(i))
print(next(i))
print(next(i))

#ジェネレータについて
#イテレータをつくる。

def counter(x):
    while True:
        yield x
        x += 1
c = counter(1)
print(next(c))
print(next(c))
print(next(c))
print("途中の処理")     #途中に処理が挟んでも前の処理を記憶しいる。
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
