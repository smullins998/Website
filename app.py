from flask import Flask, render_template, request, session
import random


app = Flask(__name__)
app.debug = True

#Backend 
@app.route('/')
def home():
    return render_template('home.html')
 
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
