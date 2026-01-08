# DevSecOps-2 – Projet Python / Docke

  Présentation du projet
  
Ce projet a été réalisé dans le cadre du module DevSecOps afin de mettre en pratique l’intégration continue, la livraison continue et la sécurité dans un petit service applicatif en Python, containerisé avec Docker et automatisé via GitHub Actions.
​
L’objectif principal est de développer une application simple, de l’exécuter dans un conteneur, et d’automatiser les vérifications (tests, qualité, sécurité) à chaque changement sur le dépôt Git.
​
  Fonctionnement global
  
L’application est écrite en Python et utilise les fichiers suivants : main.py pour la logique principale, requirements.txt pour les dépendances, un dossier templates/ pour les vues éventuelles, ainsi qu’un Dockerfile pour définir l’image d’exécution.​

Un workflow GitHub Actions (fichier dans .github/workflows/) est déclenché à chaque push sur la branche du projet afin d’installer les dépendances, lancer des commandes de vérification et éventuellement builder l’image Docker.
​

  Instructions de lancement

 A) Lancement en local
  
1) Cloner le dépôt :

  git clone https://github.com/<organisation>/DevSecOps-2.git
  cd DevSecOps-2
  git checkout main
  
2) Créer un environnement virtuel (optionnel mais recommandé) :

  python -m venv venv
  source venv/bin/activate  # sous Windows : venv\Scripts\activate
  
3) Installer les dépendances :

  pip install -r requirements.txt

4) Lancer l’application :

python main.py

  B) Lancement avec Docker
  
1) Builder l’image :

  docker build -t devsecops2-app .

2) Lancer un conteneur :

  docker run --rm -p 5678:5678 devsecops2-app

3) Accéder au service via l’URL http://localhost:5678 selon la configuration de l’application.

  Problèmes rencontrés
  
  - Problèmes de configuration du workflow GitHub Actions : erreurs d’installation de dépendances ou de version de Python non compatible.
  - Autres problèmes Github Actions : Github action reconnaît les assert pour pytest comme une erreur de sévérité low.
  - Difficultés avec la construction de l’image Docker (permissions, chemins de fichiers, dépendances manquantes ou variables d’environnement).
  - Bugs applicatifs liés à la gestion des entrées utilisateurs ou à la communication entre les composants (par exemple templates non trouvés ou erreurs d’import).

  Solutions ou contournements

  - Ajustement du fichier de workflow pour définir la bonne version de Python, installer pip et utiliser pip install -r requirements.txt.
  - Faire en sorte que le fichier yml ignore le dossier test.
  - Modification du Dockerfile pour copier correctement les fichiers nécessaires et définir un utilisateur non-root lorsque c’est possible.
  - Correction du code Python et des chemins vers les templates afin d’éviter les erreurs au lancement (tests manuels et corrections itératives).
​
  Améliorations possibles (boucle suivante)

  - Utiliser des images de base minimalistes (type alpine) pour réduire le poids du projet et supprimer les outils système inutiles qui pourraient être exploités.
  - Mettre en place un contrôle strict sur les données envoyées à l'API (longueur des textes, type de nombres) pour empêcher l'application de planter si un utilisateur envoie n'importe quoi.
  - Configurer l'API pour qu'elle renvoie des en-têtes HTTP de sécurité (comme X-Content-Type-Options) afin de mieux protéger le navigateur ou le client qui appelle l'API.
  - Ajouter une règle pour limiter le nombre de requêtes par minute depuis une même adresse IP, afin d'éviter que l'API locale ne soit saturée par des tests trop intensifs.
