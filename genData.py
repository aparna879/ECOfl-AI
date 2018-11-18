import numpy as np
from flask import Flask, render_template, request, redirect
import sqlite3
import json 

def genr(low, high, x):
    sampl = np.random.uniform(low, high, size=(x,))
    return sampl

longi = (genr(75.75,75.77,50))
lati = (genr(48.9515,48.970,50))
connection = sqlite3.connect("safai.db")
cursor = connection.cursor()
for i in range(50):
	cursor.execute("INSERT into report('name','email','lattitude','longitude') values(?,?,?,?)", ["abc"+str(i),"ab"+str(i)+"@g.com",lati[i], longi[i]])
	connection.commit()
