L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
def calc(L):
    produit = 1
    for x in L:
        if 25 <= x and x <= 90:  
            produit = produit*x
    return produit

print(calc(L))

