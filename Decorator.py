
def mod(fx):
    def modify(*arg,**kwargs):
        simp = fx(*arg,**kwargs)
        print("vah bhai jordar ho addition baki")
        return simp
    return modify


def add(a,b):
    return print(a + b) 
add(69,96)

@mod 
def hello():
    print("hey mathematician")
hello()