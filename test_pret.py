from datetime import date

# ---------- MODELES ----------

class Materiel:
    def __init__(self, reference, nom):
        self.reference = reference
        self.nom = nom
        self.disponible = True

    def __str__(self):
        statut = "disponible" if self.disponible else "emprunte"
        return f"{self.reference} - {self.nom} ({statut})"


class Emprunt:
    def __init__(self, nom, prenom, justification, materiels, prof):
        self.nom = nom
        self.prenom = prenom
        self.date = date.today()
        self.justification = justification
        self.materiels = materiels
        self.prof = prof

    def __str__(self):
        refs = ", ".join([m.reference for m in self.materiels])
        return (
            f"Emprunt par {self.prenom} {self.nom}\n"
            f"Date : {self.date}\n"
            f"Prof autorisant : {self.prof}\n"
            f"Justification : {self.justification}\n"
            f"Materiel : {refs}"
        )


# ---------- STOCKAGE ----------

inventaire = []
emprunts = []

# ---------- FONCTIONS ----------

def ajouter_materiel():
    reference = input("Reference du materiel : ")
    nom = input("Nom du materiel : ")

    inventaire.append(Materiel(reference, nom))
    print("Materiel ajoute\n")


def afficher_materiel_disponible():
    print("\nMateriel disponible :")
    for m in inventaire:
        if m.disponible:
            print(m)
    print()


def creer_emprunt():
    nom = input("Nom de l etudiant : ")
    prenom = input("Prenom de l etudiant : ")
    justification = input("Justification de l emprunt : ")
    prof = input("Nom du prof autorisant : ")

    afficher_materiel_disponible()

    refs = input("References du materiel (separees par des virgules) : ")
    refs = [r.strip() for r in refs.split(",")]

    materiels_empruntes = []

    for ref in refs:
        trouve = False
        for m in inventaire:
            if m.reference == ref and m.disponible:
                materiels_empruntes.append(m)
                m.disponible = False
                trouve = True
                break
        if not trouve:
            print(f"Materiel {ref} indisponible ou inexistant")

    if materiels_empruntes:
        emprunt = Emprunt(nom, prenom, justification, materiels_empruntes, prof)
        emprunts.append(emprunt)
        print("\nEmprunt cree :")
        print(emprunt)
    else:
        print("Aucun materiel valide selectionne")

    print()


def menu():
    while True:
        print("1 - Ajouter du materiel")
        print("2 - Voir le materiel disponible")
        print("3 - Creer un emprunt")
        print("4 - Quitter")

        choix = input("Choix : ")

        if choix == "1":
            ajouter_materiel()
        elif choix == "2":
            afficher_materiel_disponible()
        elif choix == "3":
            creer_emprunt()
        elif choix == "4":
            break
        else:
            print("Choix invalide\n")


# ---------- LANCEMENT ----------

menu()