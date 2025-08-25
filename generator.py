# import time

def chapan():
    for i in range(1,500000):
        yield i
b = chapan()
# n = time.time()
for a in b:
    print(a)
# print("the execution time in for loop    :",time.time() - n)