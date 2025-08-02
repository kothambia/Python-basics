
# a = input("enter a number:")
 
# print(f"the below calculation showa table of {a} value:")
# try:
#     for i in range(1,11):
#         print(f"{int(a)},"x",{i},"=",{int(a)*i})
# except:
#     print("input value error")

try:
    num = int(input("enter value:"))
    a =[6,3,4,5,"aryan"]
    print(a[num])
except IndexError:
    print("limit cross")
except ValueError:
    print("required integer input")


