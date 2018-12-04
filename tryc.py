
class Myexception(Exception):       #python既存のExceptionを継承
    pass
nums = [5,1,7,8,24,4]
for n in nums:
    if n > 10:
        raise Myexception(n)
#10より大きい数値が配列にある場合、例外を投げる。　２４が当てはまる。Error