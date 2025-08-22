class prani:
    def __init__(self, name, prakar):
        self.name = name
        self.prakar = prakar

    def show(self):
        print(f"""prani nu naam : {self.name}
prani no prakar: {self.prakar}""")

class biladu:
    def __init__(self,name, jati):
        prani.__init__(self, name, prakar = "biladu")
        self.jati = jati

    def show(self):
        prani.show(self)
        print(f"prani ni jati : {self.jati}")

class desibiladu:
    def __init__(self,name,color):
        biladu.__init__(self, name, jati = "desibiladu")
        self.color = color
    def show(self):
        biladu.show(self)
        print(f"kayaa rang nu {self.jati} che? :{self.color}")
a = prani("samantha","rakhadtu swaan") 
b = biladu("cateshbhai","persian")
c = desibiladu("bhimlo","kari buus")
a.show()

b.show()

c.show()
