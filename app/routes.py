from flask import render_template, redirect, url_for, request
from app import app
from app.forms import UserSubmitForm

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserSubmitForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('index.html', title='Home', form=form)

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')