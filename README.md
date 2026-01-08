# 🛡️ DevSecOps-2 | API « Tavernier – Gestionnaire de quêtes »

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black?logo=githubactions)](https://github.com/features/actions)

## 📝 Présentation du projet

Ce projet a été réalisé dans le cadre du module **DevSecOps**. L'objectif est de mettre en pratique l'intégration continue, la livraison continue et la sécurité au sein d'un service applicatif Python containerisé.

### 🍺 L'Application : Tavernier – Gestionnaire de quêtes
L'application est une **API REST** baptisée **« La Taverne du Dragon »**. Elle plonge l'utilisateur dans un univers de jeu de rôle où il peut gérer les contrats d'une taverne. L'expérience se scinde en trois sections principales :

1.  **La Porte de la Taverne (Accueil)** : La page d'entrée permettant d'accéder à l'interface de la taverne.

    <img width="2559" height="1394" alt="Capture d&#39;écran 2026-01-08 220047" src="https://github.com/user-attachments/assets/ae827a78-23ec-4d3b-ac33-dfa1f1cf1d38" />

3.  **Le Tableau des contrats** : Le cœur de l'application. Cette page affiche les contrats disponibles, permet de les accepter et de les marquer comme accomplis.

    <img width="2557" height="1392" alt="Capture d&#39;écran 2026-01-08 220111" src="https://github.com/user-attachments/assets/9397629d-c098-4a8c-9e64-248a2e07cfae" />

5.  **Le Tableau d'Affichage (Poster une quête)** : Accessible depuis le gestionnaire, cette page permet de soumettre de nouveaux contrats en précisant le **nom**, la **description** et le **montant de la récompense**.
   
    <img width="2559" height="1393" alt="image" src="https://github.com/user-attachments/assets/2b7c5496-7be4-4dc3-a6de-49c36bc1f3e0" />


### 💾 Gestion des données
Pour la persistance, l'application utilise une **base de données temporaire** (dictionnaire/liste) directement codée en Python. 
* Les quêtes initiales sont chargées au lancement.
* Les nouvelles quêtes postées via l'interface sont ajoutées dynamiquement à cette structure de données.
* L'affichage est mis à jour en temps réel sur la page du gestionnaire.

---

## 🏗️ Fonctionnement global

L’application utilise les composants suivants :
* **Logique :** `main.py` (API et gestion de la base temporaire) et `requirements.txt`.
* **Interface :** Dossier `templates/` pour le HTML, avec `static/` pour le CSS et le JS.
* **Containerisation :** Un `Dockerfile` optimisé pour la sécurité.
* **Automatisation :** Workflow GitHub Actions pour valider le code et builder l'image.

---

## 🚀 Instructions de lancement (Docker Hub)

> [!TIP]
> **Méthode recommandée :** L'image est déjà pré-construite, sécurisée et disponible publiquement sur Docker Hub.

1.  **Récupérer l'image officielle** :
    ```bash
    docker pull croustiii/devsecops_2_guardia:latest
    ```

2.  **Lancer le conteneur** :
    ```bash
    docker run --rm -d -p 5678:5678 --name tavernier-app croustiii/devsecops_2_guardia
    ```

3.  **Entrer dans la taverne** :
    > 🌐 URL locale : [http://localhost:5678](http://localhost:5678)

---

## 🛠️ Analyse Post-Déploiement

### ⚠️ Problèmes rencontrés
* ❌ **Workflow CI/CD :** Erreurs d’installation de dépendances et problèmes de compatibilité Python dans GitHub Actions.
* ❌ **Faux Positifs :** Les `assert` de `pytest` identifiés comme des failles de sécurité de sévérité **low**.
* ❌ **Docker :** Difficultés liées aux permissions système et aux chemins de fichiers internes lors du build.
* ❌ **Runtime :** Bugs de communication entre composants (templates introuvables ou erreurs d’import).

### ✅ Solutions ou contournements
* 🔧 **Optimisation YAML :** Fixation de la version Python et fiabilisation de l'étape `pip install`.
* 🔧 **Filtrage Sécurité :** Configuration du workflow pour ignorer le dossier `/test` lors de l'analyse statique.
* 🔧 **Hardening Docker :** Modification du Dockerfile pour assurer l'usage d'un utilisateur **non-root**.
* 🔧 **Débogage Applicatif :** Correction des chemins relatifs vers les templates pour garantir le rendu des pages.

---

## 📈 Améliorations possibles (boucle suivante)

> [!IMPORTANT]
> **Focus : Sécurité offensive et durcissement des données.**

* **🛡️ Images Minimalistes** : Passage sur une base **Alpine** pour réduire la surface d'attaque.
* **🛡️ Validation Strict** : Contrôle des entrées sur le formulaire de quête (type, longueur du texte, montant positif).
* **🛡️ Headers de Sécurité** : Injection de headers HTTP (ex: `X-Content-Type-Options`) pour protéger le client.
* **🛡️ Rate Limiting** : Limitation des requêtes pour éviter que la base temporaire ne soit saturée par des scripts.

---

## 👥 Crédits & Collaborateurs

Ce projet a été développé avec passion par :

| Rôle | Nom / Pseudonyme | GitHub / Contact |
| :--- | :--- | :--- |
| **Developer / DevSecOps** | **[Alexandre Caré/Martz18]** | [@Martz18](https://github.com/Martz18) |
| **Developer / DevSecOps** | **[Axel Girard/Wolf0513]** | [@Wolf0513](https://github.com/Wolf0513) |
| **Developer / DevSecOps** | **[Hakao747]** | [@Hakao747](https://github.com/Hakao747) |

---

*Dernière mise à jour : Janvier 2026*
