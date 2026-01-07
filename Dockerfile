FROM python:3.10-slim

# Environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Création de l'utilisateur système
RUN adduser --disabled-password --gecos "" myuser

# Installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code et du dossier templates
COPY . .

# Attribution des droits à l'utilisateur non-root
RUN chown -R myuser:myuser /app

# Passage à l'utilisateur non-root pour la sécurité
USER myuser

# Exposition du port défini
EXPOSE 5678

# Commande de lancement
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5678"]