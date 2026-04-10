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
