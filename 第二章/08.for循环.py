msg = "hell-python"

for letter in msg:
    print(letter)
else:
    print("循环结束")

total = 0;
for num in range(100, 501):
    if num % 3 == 0:
        total += num
else:
    print(f"计算完毕total：{total}")

m = 10
for num in range(m):
    print("*", end="")  #不换行写法，end代表什么结尾，默认\n换行

# break:只能用在循环里，表示跳出循环 (break跳出循环，while后面的else将不会执行)
# continue: 只能用在循环里，表示跳过本次循环，进行下一次循环

while True:
    name = input("请输入用户名:")
    password = input("请输入密码:")

    if name == "" or password == "":
        print("输入的用户名密码不能为空!")
        continue
    if name == "admin" and password == "123":
        print("进入程序!!!!")
        break
    else:
        print("用户名密码错误")


