#create custom error

a = input("enter value between 5 to 9:")
b = "6"
c = "7"
d = "8"
if(str(a)=="quit"):
    print("success and exiting the wesite") 
elif(str(a)!="quit"):
    if(str(a)!=b and str(a)!=c and str(a)!=d):
        raise ValueError("not valid")
    elif(int(a)<5 or int(a)>9):
        raise ValueError("enter in between 5 and 9")
    elif(int(a)>5 and int(a)<9):
        print("thank you for your input")
else:
    ValueError("not an integer")