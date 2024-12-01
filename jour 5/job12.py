L = [7, 11, 42, 39, 2]
print(L)
def trier_liste(L):
    echange = True
    while echange:
        echange = False
        i = 0
        while i < 1000:  
            if i + 1 < 1000 and L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                echange = True
            i += 1
    return L

print(trier_liste(L))


