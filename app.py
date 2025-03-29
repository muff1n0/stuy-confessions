from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

submissions = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    title = request.form.get("title")
    themes = request.form.get("themes")
    confession = request.form.get("confession")
    author_info = request.form.get("author_info")
    submissions.append({"title" : title, "themes" : themes, "confession" : confession, "author_info" : author_info}) 
    return 200

@app.route("/fetch", methods=["GET"])
def fetch_submissions():
    return jsonify({'submissions' :submissions})

if __name__ == "__main__":
    app.run(debug=True)