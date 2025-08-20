class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class programmer(employee):
    def __init__(self, name, id , lang):
        super().__init__(name, id)
        self.lang = lang
    def __str__(self):
        return f"employee name is :{self.name},id :{self.id},Language :{self.lang}"
    def __call__(self):
        if self.lang == "python":
            print("Legend")
        elif self.lang == "c++":
            print("gay ++")
        else:
            print("lendi jevo")
    
a = programmer("ary","69","python")
print(a)
a()
b = programmer("yusuf","07","java")
print(b)
b()
c = programmer("mahi","09","c++")
print(c)
c()