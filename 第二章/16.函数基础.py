# 函数定义

def circle_area_len(radius):
    """
    计算圆形的面积和周长
    :param radius:
    :return: area, len
    """
    return round(3.14 * radius * radius, 1), round(2 * 3.14 * radius, 2)

s = circle_area_len(4)
print(s)
print(type(s))

area, len = circle_area_len(4)
print(f"圆的面积：{area}, 圆的周长：{len}")



out_line = lambda : print("----------------")
out_line()
my_sum = lambda x, y: x + y
print(my_sum(2,6))
print(sum([1,2]))








