from flask import Flask,render_template,request
from flask import url_for
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/literature")
def literature():
    return render_template("literature.html")

@app.route("/material")
def material():
    return render_template("material.html")

@app.route("/algorithms")
def performance():
    return render_template("algorithms.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/testRes", methods=["POST"])

def prd():
    
    
    #fifa = dict()
    WeakFoot = request.form["WeakFoot"]
    SkillMoves = request.form["SkillMoves"]
    Crossing = request.form["Crossing"]
    Finishing = request.form["Finishing"]
    HeadingAccuracy = request.form["HeadingAccuracy"]
    LongPassing = request.form["LongPassing"]
    Interceptions = request.form["Interceptions"]
    
    '''

    Input = pd.DataFrame(
        data=[[fifa["WeakFoot"], fifa["SkillMoves"], fifa["Crossing"], fifa["Finishing"], 
        fifa["HeadingAccuracy"], fifa["LongPassing"], fifa["Interceptions"]]],
        columns=['WeakFoot', 'SkillMoves', 'Crossing', 'Finishing', 'HeadingAccuracy', 'LongPassing', 'Interceptions'])

    
    Input['key_0.0'] = 0
    Input['key_1.0'] = 0
    Input['key_2.0'] = 0
    Input['key_3.0'] = 0
    Input['key_4.0'] = 0
    Input['key_5.0'] = 0
    Input['key_6.0'] = 0

    '''
    #output=Input.shape

    lst = [[WeakFoot,SkillMoves,Crossing,Finishing,HeadingAccuracy,LongPassing,Interceptions]]
    X = np.array(lst)
    Ans = predict(X)
    
    position = ''
    if Ans[0]==0:
        position = 'DEFENDER'
    elif Ans[0]==1:
        position = 'MIDFIELDER'
    else:
        position = 'FORWARD'
        

    return render_template('test.html',output=position)

def predict(Input):
    
    pkl_filename = "lgmb_model"
    with open(pkl_filename , 'rb') as f:
        lr = pickle.load(f)

    #Input[['WeakFoot', 'SkillMoves', 'Crossing', 'Finishing', 'HeadingAccuracy', 'LongPassing', 'Interceptions']] = Input[['WeakFoot', 'SkillMoves', 'Crossing', 'Finishing', 'HeadingAccuracy', 'LongPassing', 'Interceptions']]

    print(Input.shape)
    Prediction = lr.predict(Input)


    
    return (Prediction)

if __name__ == "__main__":
    app.run(debug=True)
