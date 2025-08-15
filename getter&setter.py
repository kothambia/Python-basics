class mymarks():
    def __init__(self,value):
        self.value = value
    def s(self):
         print(f"your value : {self.value}")

    @property
    def ten_value(self):
        return 10 * self.value
    
    @ten_value.setter
    def ten_value(self, newvalue):
        self.value = newvalue/10


a = mymarks(10)
a.ten_value = 67
print(a.ten_value)
a.s()
    