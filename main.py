from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    fromDb = db.get(word)
    if fromDb:
      jobs = fromDb
    else:
      jobs = get_jobs(word)
      db[word] = jobs
      print(db[word])
  else:
    return redirect("/")

  return render_template("report.html", SearchingBy=word, resultsNumber=len(jobs))


app.run(host="127.0.0.1")