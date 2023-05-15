from flask import Flask, render_template, request, session
import random
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

#Here is the creation of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
db = SQLAlchemy(app)

class response(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    resp = db.Column('response', db.String(500))
  
    def __init__(self, name, resp):
        self.name = name
        self.resp = resp


#Backend 
@app.route('/')
def home():
    return render_template('home.html')
 
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


#Backend 
@app.route('/portfolio', methods=['POST', "GET"])
def say_something():
    if request.method == 'POST':
        form_name = request.form['nm']
        form_response = request.form['resp']
        usr = response(form_name, '')
        final_resp = response(form_response, '')
        with app.app_context():
            db.session.add(usr)
            db.session.add(final_resp)
            db.session.commit()
         
        return render_template('portfolio.html', form_response=form_response, values=response.query.all())
    else:
        return render_template('portfolio.html')


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(port=8090)


#Hey ther