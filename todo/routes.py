from todo import app
from todo.models import Todo
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    todolist = "<ul>"
    todos = Todo.query.all()
    for todo in todos:
        todolist+=f"<ul>{todo.description}</ul>"
    todolist+="</ul>"
    
    return render_template('todos.html', todos=todos)
    #return todolist


