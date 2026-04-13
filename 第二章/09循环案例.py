import random

randint = random.randint(1, 100)
while True:
    inputnum = int(input("请输入猜的数字:"))
    if inputnum > randint:
        print(f"您输入的{inputnum}大于随机数！")
    elif inputnum < randint:
        print(f"您输入的{inputnum}小于随机数！")
    else:
        print(f"您输入的{inputnum}等于随机数！")
        break
