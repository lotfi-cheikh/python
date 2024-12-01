def verifier_pair_ou_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre pair.")
        else:
            print(f"{nombre} est un nombre impair.")
    else:
        print(f"{nombre} n'est pas un entier positif valide.")


print(verifier_pair_ou_impair(12))   
print(verifier_pair_ou_impair(9))         
print(verifier_pair_ou_impair(3.8))

