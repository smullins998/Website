from flask import Flask, render_template, request, session
import random


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





with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(port=8090)
