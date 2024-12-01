L=[10, 20,30, 20, 10, 50, 60, 40, 80, 50, 40]
def supprimer_doublons(L):
    L_sans_doublons = []  
    for element in L:  
        existe_deja = False  
        for i in L_sans_doublons:  
            if i == element:
                existe_deja = True  
        if not existe_deja:  
            L_sans_doublons.append(element)
    
    return L_sans_doublons

print(supprimer_doublons(L))

