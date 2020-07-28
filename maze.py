code = input()

if (len(code) <= 200 and len(code)>=1) :
    x = 0
    y = 0
    
    for i in code :
        if i == "L":
            x = x-1
        elif i == "R" :
            x = x+1
        elif i == "U":
            y =y+1
        elif i == "D":
            y = y-1 

    print(x,y)