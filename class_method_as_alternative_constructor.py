class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    # def show(self):
    #     print(f"{self.name},{self.salary}")

    @classmethod
    def str(cls, string):
        print(string.split("-")[0],int(string.split("-")[1]))

a1 = employee("Tushar","1500000")
# print(a1.name)
# print(a1.salary)
print(a1.__dict__)
a2 = employee.str("aryan-120000")