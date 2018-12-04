
basket = {"apple","orange","banana","apple"}            #重複したデータは読み込めない
print (basket)          

#要素が入っていれば（True）無ければ（False)
print ("banana" in basket )
print ("remon" in basket )

basket.add ("grape")            #集合リストに要素を追加する
basket.remove("banana")         #リストから要素を削除する
print (basket)

empty = set()           #　setで空のリストを作る
print (empty)           
print (type(empty))         #リストの型を調べるコマンド（type)

a = {1,2,5,10}
b = {2,3,5,8}

print (a-b)         #差集合
print (a|b)         #和集合
print (a&b)         #積集合

