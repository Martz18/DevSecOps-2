# 1. Utiliser une image Python légère
FROM python:3.10-slim

# 2. Définir le dossier de travail dans le conteneur
WORKDIR /app

# 3. Copier le fichier de dépendances
COPY requirements.txt .

# 4. Installer les outils
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier ton code (main.py)
COPY . .

# 6. Lancer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5678"]