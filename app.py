from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("CREATE TABLE posts (title, themes, confession, authorInfo)")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    title = request.form.get("title")
    themes = request.form.get("themes")
    confession = request.form.get("confession")
    author_info = request.form.get("author_info")
    
    cur.execute(f"INSERT INTO posts (title, themes, confession, authorInfo) VALUES (f{title}, f{themes}, f{confession}, f{author_info})")
    return 200

@app.route("/submissions", methods=["GET"])
def fetch_submissions():
    cur.execute("SELECT * FROM posts")
    contents = cur.fetchall()
    to_dict = [{"title" : i[0], "themes" : i[1], "confession" : i[2], "author_info" : i[3]} for i in contents]
    return jsonify({'submissions' : to_dict})

if __name__ == "__main__":
    app.run(debug=True)