from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    blog_data = response.json()
    return render_template("index.html", posts=blog_data)


@app.route("/post/<post_id>")
def get_post(post_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    blog_data = response.json()
    return render_template("post.html", posts=blog_data, id=int(post_id))


if __name__ == "__main__":
    app.run(debug=True)
