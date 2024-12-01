def verifier_signe(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("négatif")
    else:
        print("zéro")
        
print(verifier_signe(5))
print(verifier_signe(0))
print(verifier_signe(-4))

