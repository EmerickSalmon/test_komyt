```python
"""
VCenterClient: Classe pour gérer la connexion à un environnement vCenter via l'API vSphere.

Cette classe permet de créer une connexion sécurisée à un serveur vCenter en utilisant les
variables d'environnement. Elle utilise pyVim pour effectuer des opérations CRUD sur
les machines virtuelles.

Configuration requise :
- VCENTER_HOST : Adresse IP ou nom de domaine du serveur vCenter
- VCENTER_USER : Utilisateur ayant des droits d'administration
- VCENTER_PASSWORD : Mot de passe de l'utilisateur
- VCENTER_PORT : Port du serveur vCenter (par défaut 443)

Exemple d'utilisation :
    client = VCenterClient()
    connection = client.connect()
"""

import os
import pyVim.connect
from pyVim.connect import SmartConnect, SmartConnectNoSSL
from pyVmomi import vim


class VCenterClient:
    """
    Classe de gestion de la connexion au vCenter.

    Cette classe permet d'initialiser une connexion sécurisée à un serveur vCenter
    à partir des variables d'environnement.

    Attributes:
        host (str): L'adresse IP ou nom de domaine du serveur vCenter.
        user (str): Nom d'utilisateur pour la connexion au vCenter.
        password (str): Mot de passe de l'utilisateur.
        port (int): Port du serveur vCenter (par défaut 44,3).
    """

    def __init__(self, host: str = None, user: str = None, password: str = None, port: int = 443):
        """
        Initialise les paramètres de connexion au vCenter.

        Les paramètres peuvent être fournis en argument ou récupérés depuis les
        variables d'environnement.

        Args:
            host (str, optional): Adresse IP ou nom de domaine du serveur vCenter.
            user (str, optional): Nom d'utilisateur pour la connexion.
            password (str, optional): Mot de passe de l'utilisateur.
            port (int, optional): Port du serveur vCenter (défaut: 443).
        """
        # Récupération des variables d'environnement si pas fournies
        self.host = host or os.getenv("VCENTER_HOST")
        self.user = user or os.getenv("VCENTER_USER")
        self.password = password or os.getenv("VCENTER_PASSWORD")
        self.port = port or int(os.getenv("VCENTER_PORT", 443))

        # Validation des paramètres
        if not self.host:
            raise ValueError("VCENTER_HOST est requis pour la connexion.")
        if not self.user:
            raise ValueError("VCENTER_USER est requis pour la connexion.")
        if not self.password:
            raise ValueError("VCENTER_PASSWORD est requis pour la connexion.")
        if not self.port:
            raise ValueError("VCENTER_PORT est requis pour la connexion.")

    def connect(self):
        """
        Établit une connexion au serveur vCenter.

        Cette méthode vérifie que tous les paramètres sont valides et retourne une
        instance de pyVim.connect.SmartConnect.

        Returns:
            pyVim.connect.SmartConnect: Instance de connexion au vCenter.

        Raises:
            ValueError: Si les paramètres de connexion ne sont pas valides.
            Exception: Si la connexion échoue (par exemple, serveur inaccessible).
        """
        try:
            # Connexion au vCenter via l'API vSphere
            connection = SmartConnect(
                host=self.host,
                user=self.user,
                pwd=self.password,
                port=self.port,
                sslContext=None  # SSL non vérifié dans le cas de tests ou environnements non sécurisés
            )
            return connection
        except Exception as e:
            raise ConnectionError(f"Échec de la connexion au vCenter : {str(e)}")
```
