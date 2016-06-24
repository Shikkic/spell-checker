from flask import Flask, render_template, url_for, request
from checker import Checker

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
  if request.method == "POST":
    text = request.form["input"]

    return render_template("home.html", text=text)

  text = "Write something here to have it spell checked!"
  return render_template("home.html", text=text)




if __name__ == "__main__":
  app.run()
