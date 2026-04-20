#定义类
class Car:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        print("Car 初始化函数-----------------")

#创建对象
car = Car("red", "zll2")
# car.color = "red"
# car.name = "zll"
print(car)
print(car.__dict__) # 将对象中的属性以字典的形式输出
print(type(car))
