code = input()
if len(code)<20:
    x = 0
    y = 0
    for i in code :
        if  i == "z" :
            x = x+1
            if i== "z" and y>0:
                exit()
        elif i == "o":
            y = y+1
    
    if (2*x == y):
        print("Yes")
    else:
        print("No")