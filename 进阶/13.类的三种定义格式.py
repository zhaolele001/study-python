
class Car:
    pass

class People():
    pass

class Zero(object):   #object是所有的父类
    pass

class Father(object):

    def __init__(self):
        self.gender = '男'

    def somking(self):
        print("抽烟有害健康Father")

class Mather(object):

    def __init__(self):
        self.gender = '男'

    def somking(self):
        print("抽烟有害健康Mather")


class Son(Mather, Father):
    pass


son = Son()
print(f"儿子的性别:{son.gender}")
son.somking()




