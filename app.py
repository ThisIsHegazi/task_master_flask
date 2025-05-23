from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
db = SQLAlchemy(app)


class TaskMaster(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_content = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task_input = request.form["task_content"]
        new_task = TaskMaster(task_content=task_input)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/home")
        except:
            return "There was an error adding your task"
    else:
        tasks = TaskMaster.query.order_by(TaskMaster.date_created).all()
        return render_template("home.html", tasks=tasks)


@app.route("/delete/<int:task_id>", methods=["GET", "POST"])
def delete(task_id):
    task = TaskMaster.query.get_or_404(task_id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect("/home")
    except:
        return "There was an error deleting your task"


@app.route("/update/<int:task_id>", methods=["GET", "POST"])
def update(task_id):
    task_to_update = TaskMaster.query.get_or_404(task_id)
    if request.method == "POST":
        task_to_update.task_content = request.form["task_content"]
        try:
            db.session.commit()
            return redirect("/home")
        except:
            return "There was an error updating your task"

    else:
        return render_template("update.html", title="Update Task", task=task_to_update)


if __name__ == "__main__":
    app.run(debug=True)
