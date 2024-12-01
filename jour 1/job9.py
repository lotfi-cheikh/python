def stock():
    nom_produit = "frigo"
    prix_unitaire = 100  
    quantite_en_stock = 20
    print("Informations initiales sur le produit :")
    print(f"Nom du produit : {nom_produit}")
    print(f"Prix unitaire : {prix_unitaire} €")
    print(f"Quantité en stock : {quantite_en_stock}\n")
    quantite_achetee = int(input(f"Combien de {nom_produit} voulez-vous acheter ? "))
    if quantite_achetee <= quantite_en_stock:
        quantite_en_stock -= quantite_achetee
        print(f"Vous avez acheté {quantite_achetee} {nom_produit}. Il reste {quantite_en_stock} en stock.")
    else:
        print(f"Stock insuffisant ! Il n'y a que {quantite_en_stock} {nom_produit} en stock.\n")
    prix_unitaire = prix_unitaire * 1.10
    print("\nInformations après mise à jour :")
    print(f"Nom du produit : {nom_produit}")
    print(f"Prix unitaire après inflation : {prix_unitaire:.2f} €")
    print(f"Quantité en stock après achat : {quantite_en_stock}")
print(stock())

