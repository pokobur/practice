import re

programming = ["c","java","python","cobol","lisp","php","Julia","ruby","R","parl"]

pattern = r"p.*n"               # . は1字以上、　*　は0文字以上
for lang in programming:
    if re.match(pattern, lang):
        print(lang)
    else:
        print("not much") 




for lang in programming:
    if re.search("^p.....$",lang):              #　^　は先頭を指す。　$　は文字列の長さ
       i = re.search("^p.....$",lang)
       print(i)