from flask import Flask, render_template, redirect, url_for, request, jsonify
import json
import os
import webbrowser
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/selection')
def selection_sort_game():
    return render_template("selection_sort.html")

@app.route('/greedy')
def greedy_game():
    return render_template("greedy.html")

@app.route('/binary')
def binary_search_game():
    return render_template("binary_search.html")

@app.route('/leaderboard')
def leaderboard():
    file_path = "data/scores.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            scores = json.load(f)
    else:
        scores = []

    scores.sort(key=lambda x: x['score'], reverse=True)

    return render_template("leaderboard.html", scores=scores)

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.json
    print("Alınan veri:", data)

    score_entry = {
        "username": data.get("username", "Anonymous"),
        "game": data.get("game"),
        "score": data.get("score"),
        "details": data.get("details"),
    }

    file_path = "data/scores.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            scores = json.load(f)
    else:
        scores = []

    scores.append(score_entry)

    with open(file_path, "w") as f:
        json.dump(scores, f, indent=4)

    return jsonify({"message": "Score recorded ✅"})
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True, use_reloader=False)



