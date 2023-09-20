# Usa una immagine di Python 3.9 come base
FROM python:3.9

# Copia il tuo codice nell'immagine
COPY . /app

# Imposta la directory di lavoro
WORKDIR /app

# Installa le dipendenze del tuo progetto
RUN pip install -r requirements.txt

# Definisci il comando di avvio dell'app
CMD ["python", "app.py"]
