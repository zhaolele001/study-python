__all__ = ['log_my_func', 'PI']

#常量 名称全部大写
PI = 3.14159
NAME = "ZHAO LL"

def log_my_func():
    print("-" * 1000)

def log2_my_func():
    print("Hello Python" * 5)

#测试函数
#__name__: Python内置变量，表示当前的模块名称(直接运行当前模块,__name__的值为  "__main__" ;当前模块被导入时，__name__的值就是当前模块名称)
print(__name__)
#执行当前文件如下代码会执行，如果当前代码被导入，则以下代码不执行
if __name__ == '__main__':
    log_my_func()


