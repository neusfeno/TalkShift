import os
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Carga de los datos de slang desde el archivo JSON
with open("slangs.json") as f:
    slangs_data = json.load(f)

# Ruta principal
@app.route("/")
def home():
    return render_template("index.html")

# Ruta del diccionario
@app.route("/dictionary")
def dictionary():
    return render_template("dictionary.html", slangs=slangs_data)

# Ruta del traductor
@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    words = text.split()
    translated = [
        slangs_data.get(word.lower(), word) for word in words
    ]  # Traduce palabra por palabra
    return jsonify({"translated_text": " ".join(translated)})

# Ruta del generador de frases
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    words = data.get("words", [])
    generated = [
        slangs_data.get(word.lower(), word) for word in words
    ]  # Genera frases a partir de palabras
    return jsonify({"generated_text": " ".join(generated)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
