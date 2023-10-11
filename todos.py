from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///TODOS.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    desc = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.Sno} - {self.title}"

@app.route('/', methods=['GET','POST'])
def home():

    title = ''
    desc = ''
    if request.method=='POST':
        print(request.form['title'])
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('home.html', allTodo = allTodo)

@app.route('/showtodos')
def show():
    pass

@app.route('/update/<int:sno>',methods = ['GET','POST'])
def updateTodo(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(Sno = sno).first()
        todo.title = title
        todo.desc = desc  # update title with whatever is entered in the form with post req method
        db.session.add(todo)
        db.session.commit()
        return redirect('/')

    todo = Todo.query.filter_by(Sno = sno).first()
    return render_template('update.html',todo = todo)

@app.route('/delete/<int:sno>')
def deleteTodo(sno):
    deleteTodo = Todo.query.filter_by(Sno = sno).first() 
    db.session.delete(deleteTodo)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True,port=8000)