def table():  
    N = int(input("Entrez un entier N (supérieur à 0) pour afficher les tables de multiplication : "))
    if N > 0:
        for i in range(1, N + 1):
            print(f"Table de multiplication de {i}:")
            for j in range(1, 11):  
                print(f"{i} x {j} = {i * j}")
    else:
        print("Veuillez entrer un entier supérieur à 0.")

print(table())