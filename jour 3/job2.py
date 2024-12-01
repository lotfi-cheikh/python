def vote():    
    age = int(input("Entrez votre âge : "))
    if age >= 18:
        print("Tu peux voter")
    else:
        print("Tu ne peux pas voter")
        
print(vote())

