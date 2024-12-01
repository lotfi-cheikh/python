def afficher_nombres_premiers():
    for n in range(2, 1001):  
        est_premier = True
        for i in range(2, int(n ** 0.5) + 1):  
            if n % i == 0:
                est_premier = False
                
        if est_premier:
            print(n)


print(afficher_nombres_premiers())

