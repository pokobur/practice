#map(関数、リスト)
lists = [1,5,10,15]
print(list(map(lambda i:i*10 , lists)))

#filter(関数、リスト）
print(list(filter(lambda i:(i%2)==0, lists)))   #偶数を抽出
print(list(filter(lambda i:(i%2)==1, lists)))   #奇数を抽出
print(list(filter(lambda i:i, lists)))
