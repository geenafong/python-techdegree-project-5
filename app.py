from flask import Flask, request, render_template, abort, flash, redirect, url_for
import os

import forms
import models

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
@app.route('/entries')
def index():
    posts = models.Post.select().limit(100)
    return render_template('index.html', posts=posts)


@app.route('/entries/new', methods=('GET', 'POST'))
def new():
    form = forms.PostForm()
    if form.validate_on_submit():
        models.Post.create( title=form.title.data, 
                            date=form.date.data, 
                            time_spent=form.time_spent.data,
                            things_learned=form.things_learned.data,
                            resources=form.resources.data)
        return redirect(url_for('index'))
    return render_template('new.html', form=form)

@app.route('/entries/<int:post_id>')
def detail(post_id):
    posts = models.Post.select().where(models.Post.post_id == post_id)
    return render_template('detail.html', posts=posts)


@app.route('/entries/<int:post_id>/edit')
def edit(post_id):
    form = forms.PostForm()
    if form.validate_on_submit():
        models.Post.update( title=form.title.data, 
                            date=form.date.data, 
                            time_spent=form.time_spent.data,
                            things_learned=form.things_learned.data,
                            resources=form.resources.data
                          ).where(models.Post.post_id == post_id).execute()
        return redirect(url_for('index'))
    return render_template('edit.html', form=form, post_id=post_id)

@app.route('/entries/<id>/delete')
def delete():
    pass

if __name__ == '__main__':
    models.initialize()

app.run(debug=True, port = 8080, host='0.0.0.0')


