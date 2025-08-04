#code
a = str(input("please enter your message:"))

if(len(a)<4):
    a = a[1:] + a[0]
    print(a)
elif(len(a)>3):
    b = str(input("please enter six random characters:"))
    a = a[1:] + a[0]
    g = b
    b = b[0:3]
    d = g[3:6]
    c = b[0:] + a[0:] + d[0:]
    print(c)
    
else:
    raise ValueError("please enter text not numbers")

decode = str(input("you want to decode? yes or no?:"))
if (decode == "yes"):
    da = c[0:-3]
    da = da[3:]
    da = da[-1] + da[0:-1]
    print(da)
else:
    print("thank you for your response")
    




