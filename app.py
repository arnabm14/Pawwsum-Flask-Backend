from flask import Flask, render_template, url_for, request, redirect
# import sqlalchemy
from datetime import datetime
from flask import jsonify
from flask import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = sqlalchemy(app)

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    print("Working")


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
        mimetype='application/json'
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
        mimetype='application/json'
    )
    return response

@app.route('/products')
def products():
    return jsonify(json.load(open("products.json")))


if __name__ == "__main__":
    app.run(debug=True)