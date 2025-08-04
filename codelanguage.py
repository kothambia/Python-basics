
m = list(str(input("Enter your massage:")))
b = "b","o","t"
print(type(m))
if len(m)<4:
    t = m[0]
    m.remove(m[0])
    m.append(t)
    print(m)
else:
    t = m[0]
    m.remove(m[0])
    m.append(t)
    m.insert(0,b)
    m.append(b)
    print(m)