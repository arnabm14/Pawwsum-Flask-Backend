from flask import Flask, render_template, url_for, request, redirect
#from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import jsonify
from flask import json
# from flask_cors import CORS

from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
# CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Task %r>' % self.id


# @app.route('/', methods=['POST', 'GET'])
# def index():
#     return "Hello World, The Code is working"
#     if request.method == 'POST':
#         task_content = request.form['content']
#         new_task = Todo(content=task_content)

#         try:
#             db.session.add(new_task)
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue adding your task'

#     else:
#         tasks = Todo.query.order_by(Todo.date_created).all()
#         return render_template('index.html', tasks=tasks)


# @app.route('/delete/<int:id>')
# def delete(id):
#     task_to_delete = Todo.query.get_or_404(id)

#     try:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return 'There was a problem deleting that task'

# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     task = Todo.query.get_or_404(id)

#     if request.method == 'POST':
#         task.content = request.form['content']

#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue updating your task'

#     else:
#         return render_template('update.html', task=task)

@app.route('/banners')
@cross_origin()
def banner():
    # return render_template('banners.json')
    data=open("banners.json")
    dataj=json.load(data)
    response = app.response_class(
        response=json.dumps(dataj),
        status=200,
        mimetype='application/json; charset=utf-8'
    )
    return response
    print(type(json.dumps(dataj)))
          
    return json.dumps(dataj)


@app.route('/categories')
@cross_origin()
def categories():
    # return render_template('categories.json')
    data=open("categories.json")
    dataj=json.load(data)
    response = app.response_class(
        response=json.dumps(dataj),
        status=200,
        mimetype='application/json; charset=utf-8'
    )
    return response

@app.route('/products')
@cross_origin()
def products():
    data=open("products.json")
    dataj=json.load(data)
    response = app.response_class(
        response=json.dumps(dataj),
        status=200,
        mimetype='application/json; charset=utf-8'
    )
    return response
    # return jsonify(json.load(open("products.json


@app.route('/recommendations')
@cross_origin()
def products():
    data=open("products.json")
    dataj=json.load(data)
    response = app.response_class(
        response=json.dumps(dataj),
        status=200,
        mimetype='application/json; charset=utf-8'
    )
    return response
    # return jsonify(json.load(open("products.json")))



if __name__ == "__main__":
    app.run(debug=True)
