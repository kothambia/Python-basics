class student:
    def __init__(self,name,mscore,pscore):
        self.name = name
        self.mscore = mscore
        self.pscore = pscore
    def __str__(self):
        return f"{self.mscore} in Maths, {self.pscore} in pysics"
    def __add__(x,y):
        totalm = x.mscore + y.mscore 
        totalp = x.pscore + y.pscore
        return f"total of class got : {totalm} in Maths, {totalp} in pysics"


s1 = student("aryan",69,68)
print(s1)
s2 = student("tushar",69,99)
print(s2)
print(s1+s2)