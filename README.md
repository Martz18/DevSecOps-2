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
* **Interface :** Un dossier `templates/` pour le html, avec un dossier static/ pour le css et le js.
* **Containerisation :** Un `Dockerfile` définissant l'image d'exécution.
* **Automatisation :** Un workflow GitHub Actions qui s'exécute à chaque *push* pour installer les dépendances et builder l'image.

---

## 🚀 Instructions de lancement

 ## 🏗️ PARTIE I : Protocoles de Lancement

### 💻 A) Installation en Local
> **Note :** Assurez-vous d'avoir Python 3.x installé sur votre machine.

1.  **Récupération du projet**
    ```bash
    git clone [https://github.com/](https://github.com/)<organisation>/DevSecOps-2.git
    cd DevSecOps-2
    git checkout main
    ```

2.  **Configuration de l'environnement**
    ```bash
    python -m venv venv
    # Activation (Windows) :  .\venv\Scripts\activate
    # Activation (Unix)    :  source venv/bin/activate
    ```

3.  **Installation & Exécution**
    ```bash
    pip install -r requirements.txt
    python main.py
    ```

---

### 🐳 B) Lancement avec Docker
| Étape | Commande | Description |
| :--- | :--- | :--- |
| **1. Build** | `docker build -t devsecops2-app .` | Construction de l'image |
| **2. Run** | `docker run --rm -p 5678:5678 devsecops2-app` | Lancement du conteneur |
| **3. Test** | Accès via `http://localhost:5678` | Vérification service |

---

## 🛠️ PARTIE II : Analyse Post-Déploiement

### ⚠️ Problèmes rencontrés
* ❌ **CI/CD :** Conflits de versions Python dans les workflows GitHub Actions.
* ❌ **Faux Positifs :** Les `assert` de Pytest marqués comme vulnérabilités (Sévérité : Low).
* ❌ **Docker :** Erreurs de permissions et dépendances manquantes lors du build.
* ❌ **Runtime :** Erreurs d'importation et templates HTML introuvables.

### ✅ Solutions appliquées
* 🔧 **Workflow :** Stabilisation du fichier YAML avec des versions de Python explicites.
* 🔧 **Whitelist :** Configuration de l'analyseur pour ignorer le répertoire `/test`.
* 🔧 **Hardening :** Passage en utilisateur **non-root** dans le Dockerfile.
* 🔧 **Fixes :** Refactorisation des chemins relatifs pour la gestion des templates.

---

## 🚀 PARTIE III : Roadmap & Améliorations

> [!TIP]
> **Objectif : Optimisation du Score de Sécurité & Performance**

* **🛡️ Sécurisation des Images**
    * Transition vers des images **Alpine** (réduction de la surface d'attaque).
* **🛡️ Validation d'Entrée (Input Sanitization)**
    * Contrôle strict des types et longueurs de données pour prévenir les injections.
* **🛡️ Headers de Sécurité**
    * Implémentation de `X-Content-Type-Options` et `Strict-Transport-Security`.
* **🛡️ Protection DOS**
    * Mise en place d'un **Rate Limiter** par adresse IP.

---
*Dernière mise à jour : 2026*
