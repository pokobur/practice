scores = [55,89,65]
print (scores[0])
print (scores[1])
print (scores[2])

score = [11,63,90]
score[1] = 100              #ここでリスト内の特定の要素を書き換える
print (score[0])
print (score[1])
print (score[2])

print(len(scores))              #リスト内の要素数を返す　３
scores.append(25)               #リストに要素を追加する  25
print (scores)

print(len(scores))              #要素を追加した後の要素数　4

for hoge in  score:             #for文を使ってリスト内の要素をまとめて表示する
    print (hoge)



