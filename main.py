from flask import Flask, render_template, url_for, request
from lib.checker import Checker

app = Flask(__name__)
checker = Checker()

@app.route("/", methods=["GET", "POST"])
def home():
  if request.method == "POST":
    text = request.form["input"]
    text = spellcheck(text)
    return render_template("home.html", text=text)

  text = "Write something here to have it spell checked!"
  return render_template("home.html", text=text)

def spellcheck(text):
  checked = []
  for word in text.split():
    w = checker.correct(word)
    checked.append(w)
  return ' '.join(checked)


if __name__ == "__main__":
  app.run()
