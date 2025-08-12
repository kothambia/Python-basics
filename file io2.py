f = open("marks.txt")
# l = f.read()
# print(l)

i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    mathematics = line.split(",")[0]
    physics = line.split(",")[1]
    chemistry = line.split(",")[2]

    print(f"Vidhyarthi{i} na Marks of mathematics:{mathematics}")
    print(f"Vidhyarthi{i} na Marks of physics:{physics}")
    print(f"Vidhyarthi{i} na Marks of chemistry:{chemistry}")

    print(f'Vidhyarthi{i} total:{int(mathematics) + int(physics) + int(chemistry)}')
    print(line)