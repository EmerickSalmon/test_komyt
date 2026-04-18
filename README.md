# Projet CRUD pour VMware Cloud Foundation (VCF)

Ce projet Python permet d'effectuer des opérations CRUD (Create, Read, Update, Delete) sur les machines virtuelles d'un environnement VMware Cloud Foundation (VCF) via l'API vSphere.

## Fonctionnalités

- Interface CLI pour gérer les machines virtuelles
- Connexion sécurisée à vCenter via l'API vSphere
- Structure modulaire avec des modules séparés par opération (Create, Read, Update, Delete)

## Installation

1. Clonez le projet :
   ```bash
   git clone https://github.com/your-username/vcf-crud.git
   cd vcf-crud
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Créez un fichier `.env` à partir de `.env.example` :
   ```bash
   cp .env.example .env
   ```

4. Modifiez le fichier `.env` avec vos informations de connexion au vCenter.

## Utilisation

Exécutez le script principal :
```bash
python src/main.py
```

Le script affichera un menu interactif avec les options suivantes :
- 1. Créer une machine virtuelle
- 2. Lister les machines virtuelles
- 3. Mettre à jour une machine virtuelle
- 4. Supprimer une machine virtuelle
- 0. Quitter

## Documentation

- Le projet est structuré en modules clairs pour faciliter la maintenance.
- Les tests sont inclus et peuvent être exécutés avec `pytest`.

## Développement

- Les fichiers sources sont organisés dans le dossier `src/`.
- Les tests sont situés dans le dossier `tests/`.
- La documentation est générée via Sphinx.

## Notes

- Ce projet est en phase initiale. Les fonctionnalités CRUD sont actuellement des stubs.
- Les connexions réelles à vCenter ne sont pas implémentées dans les premières versions.
- L'authentification est simulée dans ce fichier initial.

## Contribuer

Pour contribuer :
1. Créez une branche.
2. Faites vos modifications.
3. Faites une pull request.

## Licence

Ce projet est sous licence MIT.
---
