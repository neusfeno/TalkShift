from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para el diccionario de slangs
@app.route('/dictionary', methods=['GET', 'POST'])
def dictionary():
    # Lista completa de slangs
    slangs = [
        {'word': 'AF', 'definition': 'As f**k, used to emphasize something.'},
        {'word': '53X', 'definition': 'Sex.'},
        {'word': 'A Karen', 'definition': 'A rude and entitled middle-aged woman.'},
        {'word': 'Ate', 'definition': 'To succeed at something or do really well.'},
        {'word': 'Bae', 'definition': 'Before anyone else; babe or baby.'},
        {'word': 'Basic', 'definition': 'Boring, average, or unoriginal.'},
        {'word': 'BF/GF', 'definition': 'Boyfriend/girlfriend.'},
        {'word': 'BFF', 'definition': 'Best friends forever.'},
        {'word': 'Big Yikes', 'definition': 'Extremely embarrassing.'},
        {'word': 'Body count', 'definition': 'The number of people someone has slept with.'},
        {'word': 'Bruh', 'definition': 'Bro or dude (gender-neutral).'},
        {'word': 'Cap', 'definition': 'Fake or a lie.'},
        {'word': 'CEO', 'definition': 'To be the "CEO of" something means to excel at it.'},
        {'word': 'Cheugy', 'definition': 'Outdated or trying too hard.'},
        {'word': 'Crashy', 'definition': 'Crazy and trashy, like a trainwreck.'},
        {'word': 'Cringe', 'definition': 'Something embarrassing or awkward.'},
        {'word': 'Crunk', 'definition': 'Getting high and drunk simultaneously.'},
        {'word': 'CU46', 'definition': 'See you for sex (text shorthand).'},
        {'word': 'Curve', 'definition': 'To reject someone romantically.'},
        {'word': 'Dayger', 'definition': 'A party during the day.'},
        {'word': 'Dead', 'definition': 'Something so funny it "killed" the speaker with laughter.'},
        {'word': 'Dope', 'definition': 'Cool or awesome.'},
        {'word': 'Emo', 'definition': 'Someone emotional or dramatic.'},
        {'word': 'Extra', 'definition': 'Over-the-top, excessive.'},
        {'word': 'Fam', 'definition': 'A group of close friends.'},
        {'word': 'Fire', 'definition': 'Amazing, trendy, or awesome.'},
        {'word': 'Fit', 'definition': 'Short for "outfit."'},
        {'word': 'Flex', 'definition': 'To show off.'},
        {'word': 'Function/Func', 'definition': 'Party.'},
        {'word': 'Ghosted', 'definition': 'To end a relationship by cutting off all communication.'},
        {'word': 'Go Off', 'definition': 'Encouraging someone to continue, usually while ranting.'},
        {'word': 'GOAT', 'definition': 'Greatest of all time.'},
        {'word': 'Gucci', 'definition': 'Good, cool, or fine.'},
        {'word': 'Gyat', 'definition': 'Big butt (a reaction like “goddamn”).'},
        {'word': 'Hangry', 'definition': 'Hungry and angry.'},
        {'word': 'Hits Different', 'definition': 'Something that feels different or more impactful than usual.'},
        {'word': 'IRL', 'definition': 'In real life, as opposed to online.'},
        {'word': 'It’s giving', 'definition': 'Used to compare or describe vibes.'},
        {'word': 'IYKYK', 'definition': 'If you know, you know.'},
        {'word': 'Kick back', 'definition': 'A small party.'},
        {'word': 'Lit', 'definition': 'Amazing, cool, or exciting.'},
        {'word': 'LMIRL', 'definition': 'Let’s meet in real life.'},
        {'word': 'Low-Key', 'definition': 'To tone something down, e.g., "I’m low-key freaking out."'},
        {'word': 'Molly', 'definition': 'Ecstasy (MDMA), a dangerous party drug.'},
        {'word': 'Mood', 'definition': 'Used to express agreement or a specific vibe.'},
        {'word': 'Netflix and chill', 'definition': 'A pretense for inviting someone over to hook up.'},
        {'word': 'No cap', 'definition': 'Totally true, no lie.'},
        {'word': 'Noob/n00b', 'definition': 'A newbie or someone bad at something.'},
        {'word': 'OK, Boomer', 'definition': 'A response to outdated ideas or attitudes.'},
        {'word': 'OMG', 'definition': 'Oh my gosh or Oh my God.'},
        {'word': 'ONG', 'definition': 'Equivalent to "I swear to God."'},
        {'word': 'Periodt', 'definition': 'Used to emphasize a statement.'},
        {'word': 'Plug', 'definition': 'Someone who provides drugs.'},
        {'word': 'Pop Off', 'definition': 'To react angrily.'},
        {'word': 'Preppy', 'definition': 'Stylish, upper-class aesthetic, sometimes conformist.'},
        {'word': 'Rager', 'definition': 'A big party.'},
        {'word': 'Ratio’d', 'definition': 'More negative feedback than positive on social media.'},
        {'word': 'Requestion', 'definition': 'A request and a question, or questioning again.'},
        {'word': 'Rizz', 'definition': 'Charisma or charm.'},
        {'word': 'Salty', 'definition': 'Bitter, upset, or agitated.'},
        {'word': 'Serving', 'definition': 'Looking good or stylish.'},
        {'word': 'Ship', 'definition': 'To support two people being in a relationship.'},
        {'word': 'Shook', 'definition': 'Extremely shocked or surprised.'},
        {'word': 'Sic/Sick', 'definition': 'Cool or awesome.'},
        {'word': 'Sigma', 'definition': 'A popular loner who stands apart from the crowd.'},
        {'word': 'Simp', 'definition': 'Someone who goes overboard for someone they like.'},
        {'word': 'Slay', 'definition': 'To be stylish or successful.'},
        {'word': 'Sleep On', 'definition': 'To underestimate someone or something.'},
        {'word': 'Sloshed', 'definition': 'Very drunk.'},
        {'word': 'Smash', 'definition': 'Casual sex.'},
        {'word': 'Snatched', 'definition': 'Looking perfect or fashionable.'},
        {'word': 'Spill the Tea', 'definition': 'To share gossip.'},
        {'word': 'Squad', 'definition': 'A close-knit group of friends.'},
        {'word': 'Stan', 'definition': 'An overzealous fan of someone or something.'},
        {'word': 'Sus', 'definition': 'Suspicious or shady.'},
        {'word': 'TBH', 'definition': 'To be honest.'},
        {'word': 'Tea', 'definition': 'Gossip or news.'},
        {'word': 'Thirsty', 'definition': 'Seeking attention.'},
        {'word': 'Throw down', 'definition': 'To throw a party.'},
        {'word': 'Throw shade', 'definition': 'To insult or criticize someone.'},
        {'word': 'Tight', 'definition': 'Close relationship or friendship.'},
        {'word': 'Tool', 'definition': 'Someone obnoxious, rude, or embarrassing.'},
        {'word': 'Tope', 'definition': 'A mix of "tight" and "dope" (cool).'},
        {'word': 'Turnt', 'definition': 'To be drunk or high.'},
        {'word': 'Vanilla', 'definition': 'Boring or basic.'},
        {'word': 'WTTP', 'definition': 'Want to trade photos?'},
        {'word': 'X', 'definition': 'Ecstasy (drug).'},
        {'word': 'Yassify', 'definition': 'A dramatic makeover with beauty filters.'},
        {'word': 'Yeet', 'definition': 'To throw something forcefully.'},
        {'word': 'YOLO', 'definition': 'You Only Live Once.'}
    ]
    return render_template('dictionary.html', slangs=slangs)


# Ruta para el traductor
@app.route('/translator', methods=['GET', 'POST'])
def translator():
    translated_text = ""
    if request.method == 'POST':
        input_text = request.form['text'].lower()
        # Traducción básica (simulada)
        translations = {
            "cool": "lit",
            "friend": "BFF",
            "amazing": "GOAT",
            "bro": "bruh"
        }
        translated_text = input_text
        for normal, slang in translations.items():
            if normal in input_text:
                translated_text = translated_text.replace(normal, slang)
    return render_template('translator.html', translated_text=translated_text)

# Ruta para el generador de frases
@app.route('/generator', methods=['GET', 'POST'])
def generator():
    generated_phrase = ""
    if request.method == 'POST':
        input_text = request.form['text'].lower()
        # Generador básico (simulado)
        words = input_text.split()
        generated_phrase = " ".join([f"{word} AF" if word == "cool" else word for word in words])
    return render_template('generator.html', generated_phrase=generated_phrase)

if __name__ == '__main__':
    app.run(debug=True)
