import json
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


# Cargar slangs desde el archivo JSON
with open('static/slangs.json', 'r', encoding='utf-8') as f:
    slangs = json.load(f)["slangs"]


# Diccionario para facilitar la traducción
slang_dict = {item["word"].lower(): item["translation"] for item in slangs}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dictionary')
def dictionary():
    return render_template('dictionary.html', slangs=slangs)


@app.route('/translator', methods=['GET', 'POST'])
def translator():
    if request.method == 'POST':
        text = request.json.get('text', '').lower()
        words = text.split()
        translated_words = [slang_dict.get(word, word) for word in words]
        translated_text = ' '.join(translated_words)
        return jsonify({"translated_text": translated_text})
    return render_template('translator.html')


@app.route('/generator', methods=['GET', 'POST'])
def generator():
    if request.method == 'POST':
        new_word = request.json.get('word', '')
        new_translation = request.json.get('translation', '')
        if new_word and new_translation:
            slangs.append({"word": new_word, "definition": "", "translation": new_translation})
            slang_dict[new_word.lower()] = new_translation
            return jsonify({"message": "Word added successfully!"})
        return jsonify({"error": "Invalid input"}), 400
    return render_template('generator.html')

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render asigna un puerto específico
    app.run(host="0.0.0.0", port=port)        # Tu app escuchará en 0.0.0.0


if __name__ == '__main__':
    app.run(debug=True)



