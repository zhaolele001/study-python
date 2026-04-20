import math

def circle_area(radius: float) -> float:
    """
    根据半径计算元的面积
    :param radius: 半径
    :return: 面积
    """
    return round(math.pi * radius**2, 2)


def circle_len(radius: float) -> float:
    """
    根据半径计算元的周长
    :param radius:
    :return: 周长
    """
    return round(2* math.pi * radius, 2)


