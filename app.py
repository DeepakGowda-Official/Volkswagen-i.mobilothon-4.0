from flask import Flask, render_template, request, jsonify # type: ignore
import random

app = Flask(__name__)

responses = {
    "happy": ["I'm glad you're feeling good! Let's keep the vibes going!", 
              "That's awesome! Do you want to listen to some upbeat music?"],
    "stressed": ["I can sense some stress. Let’s take a deep breath and relax. I heard a dog near your house tried to bark at someone, but it saw me and ran off — guess it was intimidated by my shiny appearance! How are you feeling now ", 
                 "Take a deep breath, let's calm down. Should I suggest a route with less traffic?"],
    "frustrated": ["I can tell you're frustrated. Would you like to stop for a quick break?", 
                   "Hmm, you seem upset. How about stopping by that breakfast place? People joke they serve dosas without batter! Did it calm you down"],
    "neutral": ["I hope you're having a smooth day! Anything specific you'd like to do?"],
    "tired": ["Staying alert is important — I’ll help find a place to grab a coffee if you need one!"],
    "meeting":["Oh, I see! Starting the day strong – you've got this!"]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_emotion', methods=['POST'])
def analyze_emotion():
    user_input = request.form.get('user_input')
    emotion = analyze_user_emotion(user_input)
    response = generate_response(emotion)
    return jsonify({'response': response, 'emotion': emotion})

def analyze_user_emotion(user_input):
    keywords = {
        "happy": ["good", "great", "amazing", "excited", "joy", "yeah","Thanks"],
        "stressed": ["stress", "busy", "overwhelmed", "rushed", "nervous"],
        "frustrated": ["frustrated", "angry", "upset", "irritated", "annoyed"],
        "neutral": ["okay", "fine", "alright", "normal"],
        "tired": ["sleepy", "tired"],
        "meeting":["meeting","work"]
    }
    for emotion, words in keywords.items():
        if any(word in user_input.lower() for word in words):
            return emotion
    return "neutral"

def generate_response(emotion):
    return random.choice(responses[emotion])

if __name__ == '__main__':
    app.run(debug=True)
