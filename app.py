from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Slang dictionary data (91 words)
slangs_data = {
    "af": "super",
    "53x": "sex",
    "a karen": "a rude and entitled middle-aged woman",
    "ate": "to succeed at something",
    "bae": "babe or significant other",
    "basic": "unoriginal",
    "bf/gf": "boyfriend or girlfriend",
    "bff": "best friends forever",
    "big yikes": "very embarrassing",
    "body count": "number of people someone has slept with",
    "bruh": "bro or dude",
    "cap": "lie or false",
    "no cap": "no lie or true",
    "ceo": "excellent at something",
    "cheugy": "outdated or trying too hard",
    "crashy": "crazy and trashy",
    "cringe": "awkward or embarrassing",
    "crunk": "getting high and drunk at the same time",
    "cu46": "see you for sex",
    "curve": "reject someone romantically",
    "dayger": "daytime party",
    "dead": "laughing a lot",
    "dope": "awesome or cool",
    "emo": "emotional or drama queen",
    "extra": "over the top",
    "fam": "group of friends",
    "fire": "amazing or great",
    "fit": "outfit",
    "flex": "show off",
    "function/func": "party",
    "ghosted": "cut off communication",
    "go off": "encourage someone to continue",
    "goat": "greatest of all time",
    "gucci": "good or fine",
    "gyat": "reaction to a big butt",
    "hangry": "hungry and angry",
    "hits different": "something impactful",
    "irl": "in real life",
    "it’s giving": "describing vibes or feelings",
    "iykyk": "if you know, you know",
    "kick back": "small party",
    "lit": "amazing or exciting",
    "lmirl": "let’s meet in real life",
    "low-key": "subtly or slightly",
    "molly": "ecstasy (drug)",
    "mood": "relatable situation",
    "netflix and chill": "meet up for intimacy",
    "noob/n00b": "beginner or inexperienced",
    "ok boomer": "outdated attitude",
    "omg": "oh my gosh",
    "ong": "swear to god",
    "periodt": "end of discussion",
    "plug": "drug supplier",
    "pop off": "react angrily",
    "preppy": "stylish or upper-class aesthetic",
    "rager": "big party",
    "ratio’d": "more negative feedback than positive",
    "requestion": "question again or make a request",
    "rizz": "charisma or charm",
    "salty": "bitter or upset",
    "serving": "looking good or stylish",
    "ship": "support a relationship",
    "shook": "shocked or surprised",
    "sic/sick": "cool or awesome",
    "sigma": "popular but a loner",
    "simp": "overly attentive to someone",
    "slay": "succeed or look great",
    "sleep on": "underestimate something",
    "sloshed": "very drunk",
    "smash": "casual sex",
    "snatched": "looking perfect or fashionable",
    "spill the tea": "share gossip",
    "squad": "close group of friends",
    "stan": "overzealous fan",
    "sus": "suspicious",
    "tbh": "to be honest",
    "tea": "gossip or news",
    "thirsty": "seeking attention",
    "throw down": "throw a party",
    "throw shade": "insult or criticize",
    "tight": "close relationship",
    "tool": "obnoxious or rude person",
    "tope": "tight and dope",
    "turnt": "drunk or high",
    "vanilla": "boring or basic",
    "wttp": "want to trade photos",
    "x": "ecstasy (drug)",
    "yassify": "dramatic makeover with beauty filters",
    "yeet": "throw something quickly",
    "yolo": "you only live once"
}

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Slang dictionary page
@app.route("/dictionary")
def dictionary():
    return render_template("dictionary.html", slangs=slangs_data)

# Slang translator page
@app.route("/translate")
def translate_page():
    return render_template("translate.html")

# Translation API
@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    words = text.split()
    translated = [slangs_data.get(word.lower(), word) for word in words]
    return jsonify({"translated_text": " ".join(translated)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
