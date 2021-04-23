from flask import Flask
from flask import json
from flask import request

app=Flask(__name__)

@app.route('/')
def home():
    return 'hi this is home page'
    
@app.route('/github',methods=['POST'])
def message():
    if request.headers['Content-Type']=='application/json':
        return json.dumps(request.json)
    

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
