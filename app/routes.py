from flask import render_template, request, redirect
from .models import Todo

def register_routes(app, db):

    @app.route('/',methods=['GET','POST'])
    def index():
        if request.method == 'POST':

            task = request.form['task']
            # desc = request.form['desc']
            todo = Todo(task=task)
            db.session.add(todo)
            db.session.commit()

        todos = Todo.query.all()
        print(todos)
        return render_template("index.html",todos=todos)
        # return render_template("index.html")
    
    @app.route('/update/<int:todo_id>', methods=['GET', 'POST'])
    def update(todo_id):
        if request.method == 'POST':
            task = request.form.get('task')
            # desc = request.form.get('desc')
            todo = Todo.query.filter_by(todo_id=todo_id).first()
            todo.task = task
            # todo.desc = desc
            db.session.add(todo)
            db.session.commit()
            return redirect('/')

        todo = Todo.query.filter_by(todo_id=todo_id).first()
        return render_template("update.html",todo=todo)

    @app.route('/todo_status/<int:todo_id>', methods=['POST'])
    def status(todo_id):
        todo = Todo.query.get_or_404(todo_id)  # Get the todo item or 404 if not found
        status = request.form.get('status') == 'True'  # Convert the string to a boolean
        todo.status = status
        db.session.commit()  # Save the changes
        return redirect('/')

    @app.route('/delete/<int:todo_id>')
    def delete(todo_id):
        todo = Todo.query.filter_by(todo_id=todo_id).first()
        db.session.delete(todo)
        db.session.commit()
        return redirect('/')
        
    @app.route('/about')
    def about():
        return render_template('about.html')
    
    @app.route('/contact')
    def contact():
        return render_template('contact.html')
