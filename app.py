import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Diccionario de slangs
slangs_data = {
    "af": "super",
    "53x": "sex",
    "a karen": "a rude and entitled middle-aged woman",
    "ate": "succeeded greatly",
    "bae": "before anyone else",
    "basic": "boring or unoriginal",
    "bf/gf": "boyfriend or girlfriend",
    "bff": "best friends forever",
    "big yikes": "extremely embarrassing",
    "body count": "number of people someone has slept with",
    "bruh": "bro or dude",
    "cap": "a lie",
    "ceo": "someone who excels at something",
    "cheugy": "trying too hard or out of date",
    "crashy": "crazy and trashy",
    "cringe": "awkward or embarrassing",
    "crunk": "crazy and drunk",
    "cu46": "see you for sex",
    "curve": "reject someone romantically",
    "dayger": "a party during the day",
    "dead": "something so funny it 'killed' you with laughter",
    "dope": "cool or awesome",
    "emo": "emotional or dramatic",
    "extra": "over-the-top",
    "fam": "close friends or family",
    "fire": "amazing or awesome",
    "fit": "outfit",
    "flex": "to show off",
    "function/func": "a party",
    "ghosted": "cut off communication",
    "go off": "to continue with intensity",
    "goat": "greatest of all time",
    "gucci": "good or cool",
    "gyat": "goddamn or thick",
    "hangry": "hungry and angry",
    "hits different": "feels different or impactful",
    "irl": "in real life",
    "it's giving": "describing a vibe or style",
    "iykyk": "if you know, you know",
    "kick back": "a small party",
    "lit": "amazing or exciting",
    "lmirl": "let's meet in real life",
    "low-key": "subtly or moderately",
    "molly": "MDMA, a party drug",
    "mood": "agreeing with a vibe",
    "netflix and chill": "a pretense for hooking up",
    "no cap": "totally true",
    "noob/n00b": "a newbie or inexperienced person",
    "ok, boomer": "dismissive to outdated ideas",
    "omg": "oh my gosh",
    "ong": "on god, or I swear",
    "periodt": "emphasizing a statement",
    "plug": "someone who provides drugs",
    "pop off": "to express anger",
    "preppy": "stylish or upper-class",
    "rager": "a big party",
    "ratio'd": "more negative responses than positive",
    "requestion": "to question again",
    "rizz": "charisma or charm",
    "salty": "bitter or upset",
    "serving": "looking good or stylish",
    "ship": "support a relationship",
    "shook": "shocked or surprised",
    "sic/sick": "cool or awesome",
    "sigma": "a popular but independent person",
    "simp": "someone overly eager for another",
    "slay": "to succeed or look amazing",
    "sleep on": "underestimate",
    "sloshed": "drunk",
    "smash": "casual sex",
    "snatched": "perfect or fashionable",
    "spill the tea": "share gossip",
    "squad": "close group of friends",
    "stan": "an overzealous fan",
    "sus": "suspicious",
    "tbh": "to be honest",
    "tea": "gossip",
    "thirsty": "desperate for attention",
    "throw down": "host a party",
    "throw shade": "insult someone",
    "tight": "a close relationship",
    "tool": "an obnoxious person",
    "tope": "tight and dope",
    "turnt": "drunk or high",
    "vanilla": "boring or plain",
    "wttp": "want to trade photos",
    "x": "ecstasy",
    "yassify": "a dramatic makeover",
    "yeet": "to throw something forcefully",
    "yolo": "you only live once"
}

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
    translated = [slangs_data.get(word.lower(), word) for word in words]
    return jsonify({"translated_text": " ".join(translated)})

# Ruta del generador de frases
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    words = data.get("words", [])
    generated = [slangs_data.get(word.lower(), word) for word in words]
    return jsonify({"generated_text": " ".join(generated)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
