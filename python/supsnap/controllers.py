from flask import Flask, request, flash, url_for, redirect, render_template
from app import app
from db import db
from models import tasks

@app.route('/')
def index():
    return render_template('index.html', tasks = tasks.query.all() )

@app.route('/add', methods=['POST'])
def new():
    if request.method == 'POST':
        task = tasks(request.form['title'])

        db.session.add(task)
        db.session.commit()
    return redirect("/")

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        task = db.session.query(tasks).filter_by(id=request.form['id']).first()
        db.session.delete(task)
        db.session.commit()
    return redirect("/")
