from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample story data
story = {
    "scenes": [
        {
            "id": "scene1",
            "text": "You wake up in a dark room. What do you do?",
            "choices": [
                {
                    "text": "Turn on the light.",
                    "next_scene": "scene2"
                },
                {
                    "text": "Leave the room.",
                    "next_scene": "scene3"
                }
            ]
        },
        {
            "id": "scene2",
            "text": "The light flickers on, revealing a hidden door. Do you open it?",
            "choices": [
                {
                    "text": "Yes, open the door.",
                    "next_scene": "scene4"
                },
                {
                    "text": "No, stay in the room.",
                    "next_scene": "scene1"
                }
            ]
        },
        {
            "id": "scene3",
            "text": "You step outside and find yourself in a garden. It's beautiful!",
            "choices": [
                {
                    "text": "Explore the garden.",
                    "next_scene": "scene5"
                },
                {
                    "text": "Go back inside.",
                    "next_scene": "scene1"
                }
            ]
        },
        {
            "id": "scene4",
            "text": "You discover a treasure chest behind the door! You win!",
            "choices": []
        },
        {
            "id": "scene5",
            "text": "You see a strange figure in the garden. What do you do?",
            "choices": [
                {
                    "text": "Approach the figure.",
                    "next_scene": "scene6"
                },
                {
                    "text": "Run away.",
                    "next_scene": "scene1"
                }
            ]
        },
        {
            "id": "scene6",
            "text": "It's your long-lost friend! You hug and rejoice.",
            "choices": []
        }
    ]
}

@app.route('/api/story', methods=['GET'])
def get_story():
    return jsonify(story)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
