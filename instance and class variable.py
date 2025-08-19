class employee():
    company = "Tata"
    no_of_eployees = 0
    def __init__(self, name):
        self.name = name
        self.raisee = 5
        employee.no_of_eployees += 1
    
    @classmethod
    def newcomp(self, newnamecomp):
        self.company = newnamecomp

    def show(self):
        print(f"""
              your comany name is {self.company}
              no of employees under {self.company}:{self.no_of_eployees}
              your employee name is {self.name}
              your raise amount is {self.raisee}
""")

e1 = employee("aryan")
e1.company = "Tata germany"
e1.raisee = 10
e1.show()
e2 = employee("tushar")
employee.newcomp("Bata")
e2.show()
e3 = employee("mayank")
e3.show()
