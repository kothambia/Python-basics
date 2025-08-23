import time

# def lunf():
#     for i in range(1,500):
#         print(i+1)

# def lung():
#     i = 0
#     while i<=500:
#         print(i)
#         i = i + 1
        
# n = time.time()
# lunf()
# t1 = "the execution time in for loop    :",time.time() - n
# n = time.time()
# lung()
# t2 ="the execution time in while loop   :",time.time() - n
# print (t1)
# print (t2)

t = time.localtime()

t_rightnow = time.strftime("%d-%m-%y %H:%M:%S",t)
print(t_rightnow)