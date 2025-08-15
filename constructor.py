class car():
    def __init__(self,id,name,color,body,tyre,window,company):
        self.id = id
        self.name = name
        self.color = color
        self.body = body
        self.tyre = tyre
        self.window = window
        self.company = company
    def showinfo(self):
        print(f"""                    customer Name   :       {self.name}
                    customer id     :       {self.id}
                    your car color  :       {self.color}
                    your car body   :       {self.body}
                    your car tyre   :       {self.tyre}
                    your car window :       {self.window}
                    your car company:       {self.company}
""")

class typeofcar(car):
    def show(self):
        print(f"{self.name} ni car a family car")
        
d = car("1","Hasmukhbhai","red","metalic","ffs","opencustom","walkswagon")  
d.showinfo()

a = typeofcar("2","Tushar Rathva","green","fiber","mrf","matblack","bmw")
a.showinfo()
a.show()

b = car("3","Aryan Kotham","black","platinum","opollo","default","gj23bombaridino")
b.showinfo()
