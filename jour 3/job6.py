def nombre():    
    nombre = int(input("Veuillez entrer un nombre entier : "))
    if nombre % 2 == 0:
        print(f"Le nombre {nombre} est pair.")
    else:
        print(f"Le nombre {nombre} est impair.")
print(nombre())
