from flask import Flask
import sqlite3

app = Flask(__name__)
query = "SELECT quote, author FROM quotes ORDER BY random() LIMIT 1;"

@app.route("/")
def index(): 

    con = sqlite3.connect("data\data.db")
    cur = con.cursor()
    response = cur.execute(query).fetchone()

    return f"<blockquote>{response[0]} &mdash;<footer>{response[1]}</footer></blockquote>"