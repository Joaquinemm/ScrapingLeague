from flask import Flask, render_template, jsonify, send_from_directory
from tablaChampions import traerData
import json
import os

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/data/data.json')
def get_data():
    return send_from_directory('data', 'data.json')

@app.route('/tablaChampions')
def tablaChampions():
    return render_template("tabla.html")


if __name__ == '__main__':
    traerData()
    app.run(debug=True)
