from flask import Flask
from flask import json
from flask import request
from flask import jsonify
app=Flask(__name__)

@app.route('/')
def home():
    return 'hi this is home page'
    
@app.route('/github',methods=['POST'])
def message():
    if request.headers['Content-Type']=='application/json':
        info=json.dumps(request.json)
        print(info)
        print("Hi, just testing! 3nd time")
        return info
    
@app.route('/jsonobj')
def jsonobj():
   return jsonify({"sale_price":5, "actual_price" : 50, "typeofattire" : "T-Shirt", "brand" : "Nike"})


if __name__=='__main__':
    app.run(debug=True)
