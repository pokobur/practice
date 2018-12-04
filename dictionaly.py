
dic = {"A":11,"B":45,"C":90,"D":67}
print (dic)
print(dic["A"])

dic["D"] = 100          #"D"の要素を変更する　100
print (dic)
print(dic["D"])

del(dic["A"])           #"A"の要素を削除する
print(dic)

dec = {}            #空の辞書リストを作る二つの方法　
dac = dict()

print(dec)
print(dac)


for s in dic,dec,dac:           #for文ですべてのリストを表示する
    print (s)