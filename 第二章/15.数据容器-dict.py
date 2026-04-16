#字典  key 不可重复  重复后面会覆盖前面的值

#key 必须是不可变

dict1 = {"zll": 456, "hll": 789, "zll": 4568,}
print(dict1)
print(type(dict1))
print(dict1["zll"])
print(dict1["hll"])