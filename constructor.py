class car():
    def __init__(self,id,name,color,body,tyre,window,company):
        self.id = id
        self.name = name
        self.color = color
        self.body = body
        self.tyre = tyre
        self.window = window
        self.company = company
        
d = car("1","Hasmukhbhai","red","metalic","ffs","opencustom","walkswagon")  
print(f"""                    customer Name   :       {d.name}
                    customer id     :       {d.id}
                    your car color  :       {d.color}
                    your car body   :       {d.body}
                    your car tyre   :       {d.tyre}
                    your car window :       {d.window}
                    your car company:       {d.company}
""")     

a = car("2","Tushar Rathva","green","fiber","mrf","matblack","bmw")
print(f"""                    customer Name   :       {a.name}
                    customer id     :       {a.id}
                    your car color  :       {a.color}
                    your car body   :       {a.body}
                    your car tyre   :       {a.tyre}
                    your car window :       {a.window}
                    your car company:       {a.company}
""")
b = car("3","Aryan Kotham","black","platinum","opollo","default","gj23bombaridino")

print(f"""                    customer Name   :       {b.name}
                    customer id     :       {b.id}
                    your car color  :       {b.color}
                    your car body   :       {b.body}
                    your car tyre   :       {b.tyre}
                    your car window :       {b.window}
                    your car company:       {b.company}
""")