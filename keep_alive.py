# Modules - flask - threading
from flask import Flask
from threading import Thread

# Création de l'application Flask
app = Flask('')

# Définition de la route principale
@app.route('/')
def home():
    return "Le bot Discord a été pingé !"

# Fonction pour démarrer l'application Flask
def run():
    app.run(host='0.0.0.0', port=8080)

# Fonction pour maintenir l'application Flask en ligne dans un thread séparé
def keep_alive():
    t = Thread(target=run)
    t.start()
