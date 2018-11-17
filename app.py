from flask import Flask, render_template, request, redirect
import sqlite3
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def kachra():
    return render_template("index.html")

@app.route('/',methods = ['POST', 'GET'])
def report():
    if request.method == 'POST' and request.form.get('submit1')=="submit": 
        connection = sqlite3.connect("safai.db")
        cursor = connection.cursor()   
        name1 = request.form.get("name")
        email1 = request.form.get("email")
        lat1 = request.form.get("lat")
        lng1 = request.form.get("lng")
        severity1 = request.form.get("severity")
        param = (name1,email1,lat1,lng1,severity1)
        cursor.execute("INSERT INTO report(name,email,lattitude,longitude,severity) values(?,?,?,?,?)",param)
        connection.commit()
        return render_template("/index.html")

if __name__ == '__main__':
   app.run(debug = True)


