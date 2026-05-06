"""
    在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数
    这种：使用外部函数变量的内部函数称为闭包

    格式:
        def 外部函数名(形参列表):
            外部函数的（局部）变量

            def 内部函数名(形参列表):
                使用外部函数变量

            return 内部函数名(对象)

    前提条件:
    1.有嵌套  外部函数嵌套内部函数
    2.有引用  内部函数引用外部函数变量
    3.有返回  返回内部函数
    需求：定义函数保存变量10，调用函数返回值 并重复累加数值，观察结果。

    细节：函数名  和 函数名()  是两个概念 前者是对象 后者是变数
"""
def fun_outer(num1):
    def fun_inner(num2):
        sum = num1 + num2
        print(f"求和结果：{sum}")
    return fun_inner

fun_inner = fun_outer(10)
fun_inner(20)
print("*" * 100)

fun_outer(1100)(200)

"""
    nonlocal : 声明能让内部函数修改外部函数的变量
"""
def fun_outer1():
    a = 100
    def fun_inner2():
        nonlocal a
        a = a + 1
        print(f"a的值:{a}")
    return fun_inner2

if __name__ == '__main__':
    fun_inner = fun_outer1()
    fun_inner()
    fun_inner()
    fun_inner()
    fun_inner()

