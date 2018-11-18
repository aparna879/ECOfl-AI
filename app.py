from flask import Flask, render_template, request, redirect
import tsp
import sqlite3
import json, requests
from dbs import cluster
from math import sin, cos, sqrt, atan2
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
        
        param = (name1,email1,lat1,lng1)
        cursor.execute("INSERT INTO report(name,email,lattitude,longitude) values(?,?,?,?)",param)
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

@app.route('/admin1',methods = ['POST', 'GET'])
def report1():
    if request.method == 'POST' and request.form.get('cl')=="clr":
        x=cluster()
        print(x)
        # print(len(x))
        adj=[]
        
        for iter1 in range(len(x[0])):
            # source = (x[iter1][0],x[iter1][1])
            temp=[]
            for iter2 in range(len(x[0])-iter1):
                
                R = 6373.0

                lat1 = x[0][iter1];
                lon1 = x[1][iter1];
                lat2 = x[0][iter2];
                lon2 = x[1][iter2];

                dlon = lon2 - lon1
                dlat = lat2 - lat1
                a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
                c = 2 * atan2(sqrt(a), sqrt(1-a))
                distance = R * c
                temp.append(distance)
                # print( distance)
            adj.append(temp)    
        print(adj)

    return render_template("test.html",x=x)

# @app.route(/cluster)
# def cl():





if __name__ == '__main__':
    app.run(debug=True)