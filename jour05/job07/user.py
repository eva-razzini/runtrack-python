mot = input("Entrez un mot sans espace ni caractère spécial : ")
mot = mot.lower()
if not mot.isalpha():
    print("Le mot ne doit contenir que des lettres de l'alphabet !")
else:
    liste_mot = list(mot)
    for i in range(len(liste_mot)-1, 0, -1):
        if liste_mot[i] < liste_mot[i-1]:
            j = i
            while j < len(liste_mot) and liste_mot[j] < liste_mot[i-1]:
                j += 1
            liste_mot[i-1], liste_mot[j-1] = liste_mot[j-1], liste_mot[i-1]
            liste_mot[i:] = sorted(liste_mot[i:])
            break
    mot_modifie = ''.join(liste_mot)
print("Le mot modifié est : ", mot_modifie)