from flask import Flask
from flask import json 
from flask import jsonify, make_response

app=Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/banners')
def banner():
    data=open("banners.json")
    dataj=json.load(data)
    response = app.response_class(
        response=json.dumps(dataj),
        status=200,
        mimetype='application/json'
    )
    return response
    # print(type(json.dumps(dataj)))
          
    # return json.dumps(dataj)


@app.route('/categories')
def categories():
    data=open("categories.json")
    dataj=json.load(data)
    response = app.response_class(
        response=json.dumps(dataj),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/products')
def products():
    return jsonify(json.load(open("products.json")))

if __name__=="__main__":
    app.run(debug=True)