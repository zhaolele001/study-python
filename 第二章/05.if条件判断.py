# if条件判断  如果分数超过680，我就去读清华
socre = 680
if socre >= 680:
    print(f"分数:{socre}可以去读清华")
    print("欢迎您！")
print("----------------------------")

"""
登录判断
name = "赵乐乐"
password = "123"
inputname = input("请输入您的姓名:")
inputpassword = input("请输入您的密码:")

if inputname == name and inputpassword == password:
    print(f"您的账户{name},密码{password},输入正确!")

if inputname != name or inputpassword != password:
    print(f"您的账户{name},密码{password},输入不正确!")
"""

num = int(input("请输入数字:"))
if num > 0:
    print(f"{num}是正数")
elif num == 0:
    pass
else:
    print(f"{num}是负数")

