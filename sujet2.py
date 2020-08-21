def divider (x):
    while (x>=10):
        chaine=str(x)
        y = 0
        for i in range (0, len(chaine)):
            y=y+chaine[i]
        x=y
    if ((x==3) | (x==6) | (x==9)):
        return True
    else:
        return False

