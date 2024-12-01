L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
def somme_pair(L):
    Vpair = 0
    for i in L:
        if i%2 == 0:
            Vpair = Vpair + i
    return Vpair
print(somme_pair(L))

