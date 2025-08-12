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
nonv = list(filter(lambda x: x in nonveg,n))

if nonv:
    print("you are non vegetarian very good:",nonv)
else:
    vegv = list(filter(lambda x: x in veg,n))
    print("you are vegetarian very good:",vegv)