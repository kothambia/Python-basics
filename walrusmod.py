# a = True
# print(a := False)

food = []

# while True:
#     f = input("enter your favorite food:").lower()
#     if f == "quit":
#         break
#     food.append(f)
# print(food)

while (f := input("enter your favorite food:").lower()) != "quit":
    food.append(f)
print(food)

