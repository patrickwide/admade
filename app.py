from flask import Flask,render_template,request,redirect,session,jsonify,json
#import pymysql
import re
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "ssfks6787"#just a rundom string of characters.


UPLOAD_FOLDER = "static/img"
ALLOWED_EXTENSIONS = {'png','jpg','jpeg','gif','svg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=4900)
