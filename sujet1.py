
def Majuscule (chaine):
    for i in range (0, len(chaine)):
        if ((int(ord(chaine[i]))>=97) & (int(ord(chaine[i])<= 122))):
            chaine[i] =  chr(ord(chaine[i]) -32)
    return chaine