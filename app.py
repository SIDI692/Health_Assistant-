import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenue sur mon site déployé avec Render 🚀"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render fournit la variable PORT
    app.run(host="0.0.0.0", port=port)
