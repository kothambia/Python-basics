
def double(x):
    return x*x
print(double(4))

double = lambda x: x*x
print(double(6))

cube = lambda x: x*x*x
print(cube(3))

average = lambda x,y,z: (x+y+z)/3
print(average(98,88,78))

def mode(fn,value):
    return 4 + fn(value)
print(mode(cube,7))


# def sub(x,y):
#     sub = x - y
#     return sub

# sub = lambda x,y: x - y
# print(sub(69,60))

# def cube(x):
#     x = x*x*x
#     return x
# cube = lambda x: x*x*x
# # print(cube(5))

# def task1(fn,value):
#     task1 = fn-value
#     return task1

# print(task1(cube(5),3))

