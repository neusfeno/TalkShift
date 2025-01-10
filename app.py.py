from flask import Flask, render_template, request
import json
import random

# Crear la aplicación Flask
app = Flask(__name__)

# Cargar el archivo JSON con los slangs
with open('slangs.json', 'r', encoding='utf-8') as file:
    slangs_data = json.load(file)["slangs"]

# Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para el diccionario de slangs
@app.route('/dictionary', methods=['GET', 'POST'])
def dictionary():
    query = request.form.get('query', '').lower()  # Capturar búsqueda del formulario
    if query:
        # Buscar slangs que coincidan con el término
        results = [slang for slang in slangs_data if query in slang['word'].lower()]
    else:
        # Mostrar todos los slangs si no hay búsqueda
        results = slangs_data
    return render_template('dictionary.html', slangs=results)

# Ruta para el traductor de slangs
@app.route('/translator', methods=['GET', 'POST'])
def translator():
    if request.method == 'POST':
        text = request.form.get('text', '')  # Capturar texto ingresado por el usuario
        words = text.split()  # Dividir el texto en palabras
        translated = []  # Lista para construir la nueva frase

        # Recorrer cada palabra e intentar traducirla
        for i, word in enumerate(words):
            # Buscar si la palabra exacta coincide con algún slang
            slang_match = next((slang for slang in slangs_data if slang['word'].lower() == word.lower()), None)
            if slang_match:
                # Si hay un slang, reorganiza la frase con su definición
                if i > 0:  # Si no es la primera palabra
                    translated[-1] = f"{slang_match['definition']} {translated[-1]}"
                else:  # Si es la primera palabra
                    translated.append(slang_match['definition'])
            else:
                # Si no es un slang, agregar la palabra original
                translated.append(word)

        # Unir las palabras traducidas en una nueva frase
        return render_template('translator.html', original=text, translated=' '.join(translated))
    
    return render_template('translator.html')

# Ruta para el generador de frases predictivo
@app.route('/generator', methods=['GET', 'POST'])
def generator():
    if request.method == 'POST':
        input_text = request.form.get('text', '').lower()  # Capturar texto ingresado
        suggestions = []
        
        if input_text:
            # Buscar slangs relacionados con el texto ingresado
            suggestions = [
                slang for slang in slangs_data
                if input_text in slang['word'].lower() or input_text in slang['definition'].lower()
            ]
        
        return render_template('generator.html', input_text=input_text, suggestions=suggestions)
    
    return render_template('generator.html', input_text='', suggestions=[])

# Inicia la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
