import sqlite3
from flask import Flask, app, render_template, request, g, escape
import db

app = Flask(__name__)
DATABASE = './owasp-top10.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.route("/")
def mainView():
    return render_template('index.html')


# XSS
@app.route("/xss/")
def injection():
    return render_template('xss.html')


@app.route("/xssUnsecure", methods=['POST'])
def injectionUnsecure():
    name = request.form.get('nameUnsecure')
    return name


@app.route("/xssSecure", methods=['POST'])
def injectionSecure():
    name = request.form.get('nameSecure')
    escapedName = escape(name)
    return escapedName


# Injection
@app.route("/sql-injection")
def sql_injection():
    return render_template('sql_injection.html')


@app.route("/listAllUsers", methods=['GET'])
def query_all_users():
    conn = get_db()
    users = dict(conn.execute('SELECT * FROM users;').fetchall())
    # return users
    return render_template('sql_injection.html', users=users)


@app.route("/addUserToDBUnsecure", methods=['POST'])
def add_user_to_db():
    conn = get_db()
    users = (request.form.get('addNameUnsecure'),)
    cur = conn.cursor()
    cur.executescript("""
    INSERT INTO users(username) VALUES('%s')
    """ % users)
    conn.commit()
    return render_template('sql_injection.html')


@app.route("/addUserToDBSecure", methods=['POST'])
def securely_add_user_to_db():
    conn = get_db()
    users = (request.form.get('addNameSecure'),)
    sql = ''' INSERT INTO users(username)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, users)
    conn.commit()
    return render_template('sql_injection.html')


@app.route("/reset_db", methods=["POST"])
def reset_db():
    db.initiate_db()
    return render_template('sql_injection.html', reset_message='Success!')
