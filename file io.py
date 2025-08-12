
f = open("File IO operations/score.txt", "r")
f.seek(17)
l = f.read(5)
L = int(l)

a = int(input("enter new highscore(only six digits max):"))
name = str(input("enter your gammer tag:"))
if a > L:
    f = open("File IO operations/score.txt",'w')
    lines = [f"Highest score is: {a}\n",f" Gammer tag:{name}\n"]
    f.writelines(lines)
    f.close()
    f = open("File IO operations/score.txt", "r")
    n = f.read()
    print("congratulations on your new highscore:",n)
else:
    print("sorry the current highscore is:",L)

    
    
    # n = F'__{name}__'
    # f = open("score.txt", "a")
    # f.write(n)









