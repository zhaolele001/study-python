#列表操作    有序、重复、可修改
#定义
var = [56, 78, "赵乐乐", True, False]
print(type(var))

#访问列表

#获取
print(var[0]) #正向索引  从0开始
print(var[-5]) #反向索引  从-1开始

#新增

#编辑
print(var)
var[2] = "袁晨洁"
print(var)
#删除
del var[1]
print(var)
#遍历
for item in var:
    print(item)

#切片
print(var[0:3:1])
print(var[:3:1])
print(var[:3:])
print(var[:3])
print(type(var[0:3]))
