from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

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
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = get_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")

  return render_template("report.html", SearchingBy=word, resultsNumber=len(jobs), jobs=jobs)

@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    print(word)
    if not word:
      print("this is word error")
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    
    if not jobs:
      print("this is job error")
      raise Exception()
    save_to_file(jobs)
    return send_file("jobs.csv")
  except:
    print("why occur this error..")
    return redirect("/")

   
      
app.run(host="127.0.0.1")