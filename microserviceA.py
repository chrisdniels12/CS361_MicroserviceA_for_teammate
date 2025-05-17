from flask import Flask, request, jsonify, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/popularity', methods=['GET'])
def get_popularity():
    character = request.args.get('characterName')
    data = {
    "Iron Man": {"popularityScore": 92, "rank": 5},
    "Spider-Man": {"popularityScore": 98, "rank": 1},
    "Captain America": {"popularityScore": 90, "rank": 7},
    "Thor": {"popularityScore": 89, "rank": 8},
    "Hulk": {"popularityScore": 91, "rank": 6},
    "Black Widow": {"popularityScore": 88, "rank": 9},
    "Doctor Strange": {"popularityScore": 86, "rank": 10},
    "Black Panther": {"popularityScore": 95, "rank": 3},
    "Wolverine": {"popularityScore": 93, "rank": 4},
    "Deadpool": {"popularityScore": 94, "rank": 2},
    "Scarlet Witch": {"popularityScore": 87, "rank": 11},
    "Ant-Man": {"popularityScore": 84, "rank": 13},
    "Vision": {"popularityScore": 83, "rank": 14},
    "Captain Marvel": {"popularityScore": 85, "rank": 12},
    "Hawkeye": {"popularityScore": 80, "rank": 15}
}

    if character in data:
        result = data[character]
        result["character"] = character
        return jsonify(result)
    else:
        return jsonify({"error": "Character not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)