import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import plotly.graph_objects as go


mfcc_df = pd.read_csv('Datasets/MFCC_DF.csv').iloc[:,1:]
label_df = pd.read_csv('Datasets/LABEL_DF.csv').iloc[:,1:]




def RF():

    model = RandomForestClassifier()
    return model


def KNN():

    model = KNeighborsClassifier(n_neighbors=11, metric='euclidean')
    return model


def SVM():
    model = SVC(kernel='rbf', C=1, probability=True)
    return model

def MLP():
    
    model = MLPClassifier(hidden_layer_sizes=(100,), alpha=5, activation='relu', max_iter=200, solver='adam')
    model.out_activation_ = 'softmax'
    return model



def RunPlot(function):
    mfcc_df = pd.read_csv('Datasets/MFCC_DF.csv').iloc[:,1:]
    label_df = pd.read_csv('Datasets/LABEL_DF.csv').iloc[:,1:]

    X_train, X_test, y_train, y_test = train_test_split(mfcc_df, label_df, test_size=0.3)
    x_sc = StandardScaler()
    X_train = x_sc.fit_transform(X_train)
    X_test = x_sc.transform(X_test)

    model = SVC(kernel='rbf', C=1, probability=True)
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc= accuracy_score(y_pred, y_test)
    
    rep_dict = {"Drake": 0, "Post Malone": 1, "The Weekend": 2, "SZA": 3, "Taylor Swift": 4, "Kanye West": 5, "Juice WRLD": 6, "Travis Scott":7, "Lil Uzi Vert": 8}

    xx = pd.DataFrame(model.predict_proba(X_test))
    artist_list = list(rep_dict.keys())


    fig = go.Figure()
    for i in range(9):
        fig.add_trace(go.Scatter(x=y_test[0:100], y=xx.iloc[0:100,i], mode='markers', name=artist_list[i], opacity=0.8))

    fig.update_layout(
        xaxis=dict(title='Sample Index', range=[0, len(y_test[0:100])]),  # Adjust the x-axis range
        yaxis=dict(title='SVM Probability'),
        title='SVM Probability Distribution',
        legend=dict(x=1.35, y=0.6)
    )
    

    
    plot_html = fig.to_html()

    return plot_html



    
