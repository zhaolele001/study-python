#  算数运算符: + - * / // % **
print("10 + 4 = : ", 10 + 4)  # 加
print("10 - 4 = : ", 10 - 4)  # 减
print("10 * 4 = : ", 10 * 4)  # 乘
print("10 / 4 = : ", 10 / 4)  # 除
print("10 // 4 = : ", 10 // 4)  # 整除（结果为整数）
print("10 % 4 = : ", 10 % 4)  # 取余 / 求模
print("10 ** 4 = : ", 10 ** 4)  # 幂指数 , 10的4次方

# 算术运算符的优先级 ： ** --> * / // % --> + -
print("0.1 + 10  / 4**2 : ", 0.1 + 10 / 4 ** 2)

# x = input("请输入x:")
# y = input("请输入y:")
# print("x + y = : ", float(x) + float(y))
# print("x - y = : ",float(x) - float(y))

# 请输入x:0.5
# 请输入y:0.4
# x + y = :  0.9
# x - y = :  0.09999999999999998  --->精度损失

# 赋值运算符
num = 85
num += 10
print("num += 10:", num)
num -= 10
print("num -= 10:", num)
num *= 10
print("num *= 10:", num)
num /= 10
print("num /= 10:", num)
num %= 10
print("num %= 10:", num)
num **= 3
print("num **= 10:", num)
num //= 3
print("num //= 10:", num)

#比较运算符

#逻辑运算符and or not
n = int(input("请输入一个整数:"))
print(f"{n}在10到20之间：", 10 <= n <= 20)




