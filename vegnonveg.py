i = 0
n = []
while i < 3:
    a = str(input("""please enter your favorite food from this list(any 3):
             sandwich,bread,pizza,rice,noodle,
              chiken,ham,mutton,beef,egg,fish: """)).lower()
    i = i + 1
    n.append(a)
print(n)
veg = ["sandwich","bread","pizza","rice","noodle"]
nonveg = ["chiken","ham","mutton","beef","egg","fish"]

# n = set(n)
# g = list(n.intersection(nonveg))
# h = list(n.intersection(veg))
# print("nonveg items:",g)
# print("veg items:",h)
# c = []
# while g != c:
#     print("you bloody non vegetarian")
#     break
# else:
#     print("you are vegetarian good to know") 

nonv = filter(lambda x: x in nonveg,n)
if nonv:
    print("you are non vegetarian very good:",list(nonv))
vegv = filter(lambda x: x in veg,n)
if vegv:
    print("you are vegetarian very good:",list(vegv))
