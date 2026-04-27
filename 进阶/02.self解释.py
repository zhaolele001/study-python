"""
self介绍:
    Python内置关键字，用于表示 本类当前对象
    谁调用self就是谁
"""
class Car:
    def run(self):
        print(f"我是run函数，self的值是:{self}")

    def work(self):
        print(self.run())


c1 = Car()
print(f"c1对象：{c1}")
print(f"c1对象地址值：{id(c1)}")
c1.run()

print("-" * 100)

c2 = Car()
print(f"c2对象：{c2}")
print(f"c2对象地址值：{id(c2)}")
print(c2.run())