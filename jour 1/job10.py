def prix():
    montant_investissement = 2300 
    taux_rendement = 3 
    gain_initial = montant_investissement * taux_rendement / 100
    print(f"Gain initial : {gain_initial:.2f} € (sur un investissement de {montant_investissement} € à {taux_rendement}% de rendement annuel)")
    montant_investissement += 5000
    taux_rendement += 2
    gain_apres_augmentation = montant_investissement * taux_rendement / 100
    print(f"\nAprès l'augmentation du capital de 5000 €, le montant total est maintenant de {montant_investissement} €")
    print(f"Le taux de rendement est passé à {taux_rendement}%, et le gain annuel est de {gain_apres_augmentation:.2f} €")
    montant_investissement *= 0.90
    taux_rendement -= 1
    gain_apres_retrait = montant_investissement * taux_rendement / 100
    print(f"\nAprès un retrait de 10%, le montant restant est de {montant_investissement:.2f} €")
    print(f"Le taux de rendement est désormais de {taux_rendement}%, et le gain annuel est de {gain_apres_retrait:.2f} €")

print(prix())
