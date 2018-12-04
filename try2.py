
try:
    print(10/1)
except ZeroDivisionError:
    print("０で割ってはいけません")
else:
    print("例外は発生しませんでした。")
finally:
    print("finallyは必ず実行されます。")