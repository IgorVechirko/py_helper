
var_v1 = True
print(id(var_v1))

var_v1 = False
print(id(var_v1))

var_v1 = True
print(id(var_v1))

var_v1 = False
print(id(var_v1))

list_v1 = [True, 54]
list_v2 = list(list_v1)
list_v2.append("Python")

print(list_v1)
print(list_v2)