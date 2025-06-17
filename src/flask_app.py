from flask import Flask, render_template
import sqlite3
import os

## tell flask where to find the template folder
dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "templates")

app = Flask(__name__, template_folder=dir)
query = "SELECT quote, author FROM quotes ORDER BY random() LIMIT 1;"

@app.route("/")
def index():

    con = sqlite3.connect("data/data.db")
    cur = con.cursor()
    response = cur.execute(query).fetchone()
    con.close()
    return render_template("base.html", quote=response[0], author=response[1])

