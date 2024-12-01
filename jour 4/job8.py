def afficher_aliments(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    if type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")
    if type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")
    if type == "légume" and saison == "été":
        print("artichaut, aubergine, navet")
    else:
        print("Type ou saison inconnus")

print(afficher_aliments("fruits", "hiver"))
print(afficher_aliments("fruits", "été"))
print(afficher_aliments("légume", "hiver"))  
print(afficher_aliments("légume", "été"))    
print(afficher_aliments("viande", "été"))