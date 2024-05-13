
# API de Trackey

API via Django_Rest_Framework. 

# Organisation

**Gestion des Vues :**
Les vues sont configurées à l'aide de `ModelViewSet` accompagné d'un routeur, ce qui permet de traiter l'ensemble des opérations CRUD via une interface unique. Exception faite pour les actions de connexion et de création (POST) d’un utilisateur, un accès connecté est requis pour interagir avec les autres vues. Ces dernières contrôlent également l'accès aux données en vérifiant l'identité de l'utilisateur connecté, afin de s'assurer que les données consultées correspondent à celles associées à son `user_id`. 

**Sérialisation :**
Les sérialiseurs facilitent la conversion et l'interprétation des données au format JSON. Ils jouent également un rôle crucial dans la gestion des informations accessibles à l'utilisateur, ainsi que dans la vérification de données transmises par l'user, particulièrement pour les requêtes utilisant les méthodes POST, PUT et PATCH.


**Authentification :**
L'authentification est prise en charge par `simple_jwt`, ce qui me permet, lors de la connexion, d'obtenir des jetons JWT d'accès et de rafraîchissement. Ces jetons facilitent la gestion de la session utilisateur sur l'application et permettent de vérifier l'authentification de l'utilisateur. 

L'utilisateur n'utilise pas le modèle par défaut mais est configuré dans `models.py` sous le nom `Agency`. Le jeton d'accès transmet l'ID de l'utilisateur, qui est ensuite décodé dans React et utilisé dans certaines requêtes pour récupérer exclusivement les données relatives à l'agence.

Initialement, l'objectif était de structurer chaque organisation d'agence avec une agence, un manager et un utilisateur simple. Permettant à chaque membre de l'agence d'avoir son propre compte. Cependant, j'ai rencontré plusieurs difficultés pour comprendre le fonctionnement et la gestion des droits ainsi que le partage des données au sein de l'organisation. Par conséquent, j'ai décidé de simplifier mon code, avec un code pour tous les membres de l'agence. Toutefois j'ai voulu limiter l'accès à la modification des informations d'authentification et la suppression des données via un code OTP envoyé par mail. De cette façon, seule la personne ayant son e-mail de renseigné sur le compte peut effectuer ces actions.

# Déploiement: 
L'API est en ligne via cloud sur Heroku, la base de données est gérée par PostgreSQL, et les images de chaque clé sont stockées sur AWS. 






