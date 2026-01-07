# 1. Image de base
FROM python:3.10-slim

# 2. Définir le dossier de travail
WORKDIR /app

# 3. Créer l'utilisateur (mais rester root pour l'instant)
RUN adduser --disabled-password --gecos "" api_user

# 4. Copier et installer les dépendances (en tant que root)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier le reste du code
COPY . .

# 6. Donner la propriété du dossier /app à l'utilisateur api_user
RUN chown -R api_user:api_user /app

# 7. Passer à l'utilisateur non-root pour la sécurité
USER api_user

# 8. Lancer l'application avec le préfixe "python -m" (plus robuste)
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5678"]