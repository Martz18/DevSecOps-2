# 🛡️ DevSecOps-2 | API Python & Docker

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black?logo=githubactions)](https://github.com/features/actions)

## 📝 Présentation du projet

Ce projet a été réalisé dans le cadre du module **DevSecOps**. L'objectif est de mettre en pratique l'intégration continue, la livraison continue et la sécurité au sein d'un service applicatif Python containerisé.

**Objectifs principaux :**
* 🐍 Développer une application simple en Python.
* 🐳 Exécuter l'application dans un conteneur Docker.
* ⚙️ Automatiser les vérifications (tests, qualité, sécurité) via GitHub Actions.

---

## 🏗️ Fonctionnement global

L’application utilise les composants suivants :
* **Logique :** `main.py` pour le code principal et `requirements.txt` pour les dépendances.
* **Interface :** Un dossier `templates/` pour le HTML, avec un dossier `static/` pour le CSS et le JS.
* **Containerisation :** Un `Dockerfile` définissant l'image d'exécution.
* **Automatisation :** Un workflow GitHub Actions qui s'exécute à chaque *push* pour valider le code et builder l'image.

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
    docker run --rm -d -p 5678:5678 --name devsecops-app croustiii/devsecops_2_guardia
    ```

3.  **Accéder au service** :
    > 🌐 URL locale : [http://localhost:5678](http://localhost:5678)

---

## 🛠️ Analyse Post-Déploiement

### ⚠️ Problèmes rencontrés
* ❌ **Workflow CI/CD :** Erreurs d’installation de dépendances et problèmes de compatibilité avec les versions de Python.
* ❌ **Faux Positifs :** Les `assert` de `pytest` ont été identifiés par GitHub Actions comme des erreurs de sécurité de sévérité **low**.
* ❌ **Construction Docker :** Difficultés liées aux permissions système, aux chemins de fichiers internes et aux variables d'environnement.
* ❌ **Runtime :** Bugs liés à la communication entre les composants (templates non trouvés ou erreurs d’import).

### ✅ Solutions et contournements
* 🔧 **Optimisation YAML :** Ajustement du workflow pour fixer la version de Python et fiabiliser le `pip install`.
* 🔧 **Filtrage Sécurité :** Configuration du workflow pour ignorer le dossier de tests lors de l'analyse statique.
* 🔧 **Hardening Docker :** Modification du Dockerfile pour assurer une copie correcte des fichiers et l'usage d'un utilisateur **non-root**.
* 🔧 **Débogage Applicatif :** Correction itérative du code Python et des chemins vers les templates pour garantir le lancement.

---

## 📈 Améliorations possibles (boucle suivante)

> [!IMPORTANT]
> **Focus : Sécurité offensive et optimisation des ressources.**

| Amélioration | Description | Impact |
| :--- | :--- | :--- |
| **🛡️ Images Alpine** | Utilisation de bases minimalistes pour réduire le poids. | **Sécurité ++** |
| **🛡️ Validation Strict** | Contrôle des entrées API (longueur, types, format). | **Stabilité ++** |
| **🛡️ Headers HTTP** | Ajout de headers de sécurité (ex: `X-Content-Type-Options`). | **Protection ++** |
| **🛡️ Rate Limiting** | Limitation des requêtes par IP pour éviter les saturations. | **Disponibilité ++** |

---
*Dernière mise à jour : Janvier 2026*
