from flask import Flask, render_template
from utils.github import get_followers_info, get_user_info

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/user/<username>", methods=["GET"])
def search_user(username):
	user = get_user_info(username)
	followers = get_followers_info(username)
	payload = {
		"user": user,
		"followers": followers
	}
	return render_template("user.html", data=payload)

@app.errorhandler(404)
def not_found(error):
	return render_template("404.html")
