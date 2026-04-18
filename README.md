# Projet Python pour Gestion des Machines Virtuelles VMware Cloud Foundation

Ce projet Python permet d'effectuer des opérations CRUD (Create, Read, Update, Delete) sur les machines virtuelles d'un environnement VMware Cloud Foundation (VCF) via l'API vSphere.

## Fonctionnalités

- **Create** : Création de machines virtuelles à partir de modèles définis.
- **Read** : Lecture des informations sur les machines virtuelles existantes.
- **Update** : Modification des configurations des machines virtuelles.
- **Delete** : Suppression de machines virtuelles.

## Structure du Projet

```
project/
├── src/
│   └── vcf_client/
│       ├── __init__.py
│       ├── client.py
│       └── vm_operations.py
├── tests/
│   └── test_vm_operations.py
├── requirements.txt
├── README.md
└── setup.py
```

## Utilisation

1. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

2. Configurez les paramètres de connexion (URL, credentials, etc.) dans `src/vcf_client/config.py`.

3. Exécutez les opérations CRUD :
   ```python
   from vcf_client.client import VCFClient

   client = VCFClient()
   client.create_vm("my-vm", "template")
   ```

## État d'avancement

- [x] Structure de base du projet
- [x] Implémentation des opérations CRUD
- [ ] Intégration de la gestion des erreurs
- [ ] Tests unitaires
- [ ] Documentation complète

Ce projet est conçu pour être maintenable et évolutif, prête à intégrer des fonctionnalités futures telles que la gestion des réseaux, des stockages ou des snapshots.
