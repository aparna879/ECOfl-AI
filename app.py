from flask import Flask, render_template, request, redirect
import sqlite3
import json 

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def kachra():
    return render_template("index.html")

# @app.route('/admin')
# def saaf():
#     return render_template("admin.html")


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
        return redirect("/admin")

@app.route('/admin')
def markerPlot():
    return render_template("admin.html")

@app.route('/getMarkerData')
def getMarkerData():
    connection = sqlite3.connect("safai.db")
    cursor = connection.cursor()
    cursor.execute("SELECT lattitude,longitude from report")
    #latix = cursor.fetchall()
    lati=cursor.fetchall()
    connection.commit() 
    geocode = lati[0], lati[1]
    # print(lati)
    cursor.execute("SELECT COUNT(*) from report")
    connection.commit() 
    gin_liya = cursor.fetchall()
    json_data=[]
    try:
        for latlong in lati:
            json_data.append({
                'latitude': latlong[0],
                'longitude': latlong[1]
            })
    except Exception as e:
        pass
    x=json.dumps(json_data)
    connection.commit()
    return x


if __name__ == '__main__':
    app.run(debug=True)