
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import jsonify
from flask import json
# from flask_cors import CORS

from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
# CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FName = db.Column(db.String(200), nullable=False)
    LName = db.Column(db.String(200), nullable=False)
    PName = db.Column(db.String(200), nullable=False)
    PType = db.Column(db.String(200), nullable=False)
    Email = db.Column(db.String(200), nullable=False)
    Password = db.Column(db.String(200), nullable=False)
    # content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    # return "Hello World, The Code is working"
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)

@app.route('/banners')
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
def recommend():
    data=open("products.json")
    dataj=json.load(data)
    response = app.response_class(
        response=json.dumps(dataj),
        status=200,
        mimetype='application/json; charset=utf-8'
    )
    return response
    # return jsonify(json.load(open("products.json")))

@app.route('/recommendations/<string:pt>')
def recommend_user(pt):
    # print(id) Pet Name
    data=open("products.json")
    dataj=json.load(data)
    # print(dataj[0]["name"])
    # User_id = User.query.get_or_404(pt)
    # animal=User_id.PType
    # print(type(dataj))
    l=list()
    cat=["CATS","CAT","NEKOCHAN"]
    dog=["DOGS","DOG","INU"]
    pt=pt.upper()
    if pt in cat:
        pt="CAT"
        # pts="CATS"
    elif pt in dog:
        pt="DOG"
        # pts="DOGS"
    for i in dataj:
        s=i["name"].upper().split()
        
        if (pt in s) :
            print(i["name"])
            print("*"*50)
            l.append(i)
    # print(l)
        
    response = app.response_class(
        response=json.dumps(l),
        status=200,
        mimetype='application/json; charset=utf-8'
    )
    return response
    # return jsonify(json.load(open("products.json")))

@app.route('/user/order', methods=['POST', 'GET'])
def User_Checkout():
    dataj={'Data':"Data"}
    response = app.response_class(
        response=json.dumps(dataj),
        # response="",
        status=200,
        mimetype='application/json; charset=utf-8'
    )
    return response
    

@app.route('/user', methods=['POST', 'GET'])
def User_Interaction():
    # return "Hello World, The Code is working"
    if request.method == 'POST':
        # print("Inside post")
        fn = request.form['fn']
        ln = request.form['ln']
        pn = request.form['pn']
        pt = request.form['pt']
        em = request.form['em']
        ps = request.form['ps']
        new_user = User(FName=fn,
                        LName=ln,
                        PName=pn,
                        PType=pt,
                        Email=em,
                        Password=ps,
                        )

        try:
            db.session.add(new_user)
            db.session.commit()
            # print("Done")
            return redirect('/user')
            
        except:
            return 'There was an issue adding your User'

    else:
        users = User.query.all()
        # print(users)
        return render_template('uindex.html', users=users)

@app.route('/user/delete/<int:id>')
def user_delete(id):
    task_to_delete = User.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/user')
    except:
        return 'There was a problem deleting that task'

@app.route('/user/pass/<string:email>')
def user_pasword(email):

    task_to_delete = User.query.filter_by(Email=email).first()
    if task_to_delete==None:
        return "Wrong Username or Password"
    
    return task_to_delete.Password


@app.route('/user/update/<int:id>', methods=['GET', 'POST'])
def user_update(id):
    task = User.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['FName']

        try:
            db.session.commit()
            return redirect('/user')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)

@app.route('/user/session')
def session():
    print(session["email"])

if __name__ == "__main__":
    app.run(debug=True)
