
def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3
note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : "))

moyenne_etudiant = moyenne(note1, note2, note3)

if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")
if 11 <= moyenne_etudiant < 15:
    print("Bon élève")
if 8 <= moyenne_etudiant < 11:
    print("Élève moyen")
if 0 <= moyenne_etudiant < 8:
    print("Élève devant faire des efforts")
else:
    print("Moyenne invalide")

