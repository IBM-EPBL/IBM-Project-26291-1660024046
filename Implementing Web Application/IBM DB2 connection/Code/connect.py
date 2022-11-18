
from flask import Flask,render_template,request,redirect,url_for,session
import ibm_db
import re

app=Flask(__name__)
app.secret_key='a'

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=;PORT=;Security=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=;PWD=",'','')

@app.route('/')
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run(host='0.0.0.0')
