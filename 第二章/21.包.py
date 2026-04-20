#1.导入模块
# import utils.my_fun
#
# utils.my_fun.log_my_func()
# utils.my_fun.log2_my_func()

# from utils import my_fun
#
# my_fun.log2_my_func()

#注意，要导入包下的所有模块，就必须在__init__文件中添加 __all__=[]
from utils import *

my_fun.log2_my_func()

from utils.my_fun import log_my_func
log_my_func()








