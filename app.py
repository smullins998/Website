from flask import Flask, render_template, request, session
import random

from ProbabilityChart import RunPlot
from ProbabilityChart import MLP, KNN, RF



app = Flask(__name__)
app.debug = True

#Backend 
@app.route('/')
def home():
    
    Prob_fig = RunPlot(MLP())
    
    return render_template('home.html', Prob_fig=Prob_fig)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
