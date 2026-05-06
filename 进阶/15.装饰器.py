"""
    装饰器的作用是:不改变原有函数的基础上，给原有函数增加额外功能
    装饰器本质上就是一个闭包函数

    构成条件：
    1.有嵌套 在函数嵌套(函数里面再定义函数)的前提下
    2.有引用 内部函数使用了外部函数的变量（还包含外部函数的参数）
    3.有返回 外部函数返回了内部函数名（对象）
    4，有额外功能：给需要装饰的原有函数增加额外功能

"""

def fun_outer(num):
    def fun_inner():
        nonlocal num
        num += 1
        print(num)
    return fun_inner

def check_login(fun_name):
    def fun_inner():
        print("登录种....")
        fun_name()
    return fun_inner


def comment():
    print("发表评论")

def payment():
    print("充值种.....")

@check_login
def comment2():
    print("语法糖发表评论")


login = check_login(comment)
login()
comment()
print("*"*50)
comment = check_login(comment)
comment()
print("*"*50)
f = check_login(payment)
f()

print("*"*50)
comment2()


def get_sum(*args, **kwargs):
    """
    返回和
    :param args:
    :param kwargs:
    :return:
    """
    return sum(args) + sum(kwargs.values())
    # return sum(args, kwargs.values()) 不行

if __name__ == '__main__':
    sum = get_sum(1, 2, 3, a=4, b=5, c=6)
    print(sum)
# if __name__ == '__main__':
#     fun_inner = fun_outer(8)
#     fun_inner()
#     fun_inner()
#     fun_inner()
