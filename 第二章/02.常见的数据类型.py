# 常见数据类型-->type() 获取指定的字面量或变量的类型
from types import NoneType

print("hello world")
print(type("hello world"))

print(type(10))
print(type(3.14))
print(type(True))
print(type(False))
print(type(None))

# 常见数据类型  --> isinstance(数据，类型)  --->bool值--->判断数据是否是指定的类型,如果是：True
num, type1 = 10, True
print(type(num), type(type1))

print(isinstance(num, int))
print(isinstance(type1, NoneType))

# 定义字符串3种方式

msg1 = "您好1"
msg2 = '您好2'
msg3 = """
    亲爱的body!
     :   我今天心情特别好
"""

print(msg1)
print(msg2)
print(msg3)

print(type(msg1))
print(type(msg2))
print(type(msg3))

# 转义字符
# \n  \t \' \"

print("您好，我心情好\n你帮我把\t->他拿过来八，那是：\"杯子\" 那必然很好：It's time")
print('It\'s time')

# 字符串的拼接
# 注意： +号可以用来拼接两个字符串，但是无法将非字符串与字符串进行拼接（非字符串类型需要转换为字符串类型）
slozll = "您好"    "今天星期五"
print(slozll)

slozll2 = "您好" + "今天星期八"
print(slozll2)

sg1 = "人生苦短"
sg2 = "我用java"
print("赵乐乐说:" + sg1 + "," + sg2)

# 字符串类型转换
age = 10
name = "赵乐乐"
print(name + "今年" + str(age) + "岁")

# 字符串的格式化 占位符的数量要和变量的数量保持一致
s1 = "乐哥"
s2 = 80
print("我是%s" % s1)
print("晚上今天%s，明天%s" % (s1, s2))

#方式2  ---->推荐方式
name ="赵乐乐"
print(f"{name}您好，我今天心情好")




