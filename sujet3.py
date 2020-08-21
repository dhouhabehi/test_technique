def voisinsCase (plateau, case):

#chercher la position de la case dans le plateau

    j=0
    i=0
    l=0
    k=0
    Find = False
    for i in range(0,2):
        while ((Find == False ) & (j<=len(plateau[i]))):
            if (plateau[i][j]== case):
                Find= True
                l=i
                k=j
            j+=1


    result = []
#ajouter voisins verticaux
    if (l==0):
        result.append(plateau[l+1][k])
    elif (l==1):
        result.append(plateau[l-1][k])



#ajouter voisins horizontaux
    if (k==len(plateau(l))):
        result.append(plateau[l][k-1])
    elif (k==0):
        result.append(plateau[l][k + 1])
    else:
        result.append(plateau[l][k - 1])
        result.append(plateau[l][k + 1])


#retourner le resultat
    return (result)





def voisinsCases(plateau,cases):
 #on va utiliser la fonction précèdente
    result1=[]
    for case in cases:
        result1.append(voisinsCase(case))

    return result1




def accessibles(plateau,case):

#on va utiliser la fonction précèdente
    list=voisinsCase(plateau,case)
    find=False
    result=[]

    #la première case porte sur le déplacement vertical
    if (list[0] == True):
    # dans ce cas on doit se déplacer horizontlement seulement
        i=1
        while ((find==False )&(i<=len(list))):
            if list[i]==False:
                result.append(list[i])
                i+=1
            else:
                find=True

    elif (list[0]==False):
    # dans ce cas on doit se déplacer horizontlement et verticalement
        result.append(list[0])


        i = 1
        while ((find == False) & (i <= len(list))):
            if list[i] == False:
                result.append(list[i])
                i += 1
            else:
                find = True

    return result



def chemin (plateau, caseDeb, caseFin):
    #on va calculer le nombre de case séparant la case de départ et la case d'arrivée puis on les compare avec le nombre de cases de la
    #fonction accessible


    #connaitre la position de la case de départ
    j = 0
    i = 0
    l = 0
    k = 0
    Find = False

    for i in range(0, 2):
        while ((Find == False) & (j <= len(plateau[i]))):
            if (plateau[i][j] == caseDeb):
                Find = True
                l = i
                k = j
            j += 1

    # connaitre la position de la case de départ
    j1 = 0
    i1 = 0
    l1 = 0
    k1 = 0
    Find1 = False
    for i1 in range(0, 2):
        while ((Find1 == False) & (j1 <= len(plateau[i1]))):
            if (plateau[i1][j1] == caseFin):
                Find1 = True
                l1 = i1
                k1 = j1
            j1 += 1



    pos=0
    if (l!=l1):
        pos+=1
        if (k1>k2):
            pos+=k1-k2
        elif (k2>k1):
            pos+=k2-k1
    else:
        if (k1>k2):
            pos+=k1-k2
        elif (k2>k1):
            pos+=k2-k1

    #on va utiliser la fonction accessible
    list=accessibles(plateau,caseDeb)
    cmp=len(list)

    #on va comparer les deux résultats
    if (cmp==pos):
        return True
    else:
        return False


















