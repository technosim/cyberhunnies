from flask import Flask, render_template, jsonify
import random
import os

app = Flask(__name__)

# Load options from a text file (one per line)
def load_options():
    with open("options.txt", "r") as f:
        return [line.strip() for line in f if line.strip()]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/options")
def options():
    return jsonify(load_options())

@app.route("/spin")
def spin():
    options = load_options()
    choice = random.choice(options)
    return jsonify({"result": choice})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))  # Azure sets PORT dynamically
    app.run(host="0.0.0.0", port=port, debug=True)

