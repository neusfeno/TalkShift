from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Cargar el diccionario de slangs
with open("slangs.json", "r") as file:
    slangs_data = json.load(file)

# Ruta principal
@app.route("/")
def home():
    return render_template("index.html")

# Ruta para el diccionario
@app.route("/dictionary")
def dictionary():
    return render_template("dictionary.html", slangs=slangs_data)

# Ruta para el traductor
@app.route("/translator")
def translator_page():
    return render_template("translator.html")

# API para traducir texto
@app.route("/translator", methods=["POST"])
def translator():
    data = request.get_json()
    text = data.get("text", "")
    words = text.split()
    translated = [slangs_data.get(word.lower(), word) for word in words]
    return jsonify({"translated_text": " ".join(translated)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
