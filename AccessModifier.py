class human:
    def __init__(self,name,age,color):
        self.__name = name
        self.__age = age
        self.__color = color

    def _show(self):
        print(f""" This human is {self._human__name},
               and {self._human__name} is {self._human__age} 
               years old""") 

class origin(human):
    def oshow(self):
        print("he is indian")


a = origin("aryan",69,"brown")
print(a._human__name)
print(a._human__age)
print(a._human__color)
a._show()
a.oshow()
