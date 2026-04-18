"""
Module principal du projet.

Ce script affiche un menu CLI interactif permettant d'effectuer des opérations CRUD
sur les machines virtuelles dans un environnement VMware Cloud Foundation (VCF)
via l'API vSphere.
"""

import sys
from src.client.client import VCClient


def show_menu():
    """Affiche le menu principal."""
    print("\n=== Menu CRUD pour les machines virtuelles ===")
    print("1. Créer une machine virtuelle")
    print("2. Lister les machines virtuelles")
    print("3. Mettre à jour une machine virtuelle")
    print("4. Supprimer une machine virtuelle")
    print("0. Quitter")
    print("-" * 40)


def get_user_choice():
    """Obtient le choix de l'utilisateur."""
    try:
        choice = input("Veuillez choisir une option (0-4): ").strip()
        return int(choice)
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")
        return None


def main():
    """Fonction principale du script."""
    # Exemple de configuration (à remplacer par chargement depuis .env)
    vcenter_host = "vcenter.example.com"
    vcenter_user = "admin@vsphere.local"
    vcenter_password = "securepassword"
    vcenter_port = 443

    # Initialisation du client
    client = VCClient(vcenter_host, vcenter_user, vcenter_password, vcenter_port)

    while True:
        show_menu()
        choice = get_user_choice()

        if choice == 0:
            print("Au revoir !")
            break
        elif choice == 1:
            print("Option 'Créer' sélectionnée. (Implémentation future)")
        elif choice == 2:
            print("Option 'Lister' sélectionnée. (Implémentation future)")
        elif choice == 3:
            print("Option 'Mettre à jour' sélectionnée. (Implémentation future)")
        elif choice == 4:
            print("Option 'Supprimer' sélectionnée. (Implémentation future)")
        else:
            print("Option invalide. Veuillez choisir entre 0 et 4.")


if __name__ == "__main__":
    main()
---
