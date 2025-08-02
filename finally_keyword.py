def ind():
    try:
        a = int(input("enter the number:"))
        l = [1,4,69,43,5]
        print(l[a])
        return "success"
    except:
        print("gher ja")
        return "sorry bro"
    finally:
        print("show ad")

print(ind())
