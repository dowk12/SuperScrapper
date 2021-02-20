from flask import Flask, render_template, request

app = Flask("SuperScrapper")

@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  return render_template("report.html", SearchingBy=word, potato="sexy")


app.run(host="127.0.0.1")