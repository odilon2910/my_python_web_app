FROM python:3.9-slim
WORKDIR /app
# Copier seulement le fichier requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt
# Ces deux points avec COPY copier tous les fichiers dans le projet.
COPY . .
EXPOSE 5000
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]