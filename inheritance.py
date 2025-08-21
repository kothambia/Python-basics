class employee:
    def __init__(self, name, id, skill):
        self.name = name
        self.id = id
        self.skill = skill
        
    def show(self):
        print(f"This employee's name is {self.name}, with id: {self.id}")

class work(employee): 
    def wshow(self):
        print(f"{self.name} is skilled in:{self.skill}")
        if self.skill == "coding":
            print(f"{self.name} is a programmer")
        elif self.skill == "speaking":
            print(f"{self.name} is HR")
        else:
            print(f"{self.name} is a cleaner")

a = work("Aryan",69,"coding")
a.show()
a.wshow()

b = work("Tushar",96,"speaking")
b.show()
b.wshow()

c = work("mayank",50,"cleaning")
c.show()
c.wshow()