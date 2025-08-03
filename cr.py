a = input("enter value between 5 to 9:")

if(str(a)=="quit"):
    print("success and exiting the wesite") 
elif(a.isdigit()):
    if(int(a)<5 or int(a)>9):
        raise ValueError("invalid number")
    else:
        print("thank you for your input")
else:
    raise ValueError("Enter either quit or between 5 to 9")
    