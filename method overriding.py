class ract:
    def __init__(self,w,l):
        self.w = w
        self.l = l
    def area(self):
        return self.w * self.l

class circle(ract):
    def __init__(self,r):
        self.r = r
        super().__init__(r,r)
    
    def area(self):
        return 3.14 * super().area()

# rect1 = ract(5,7)
# print(rect1.area())

cir1 = circle(6)
print(cir1.area())