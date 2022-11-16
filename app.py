import pickle
from flask import Flask,render_template,app,jsonify,request,url_for
import pandas as pd
import numpy as np

app=Flask(__name__)

model=pickle.load(open('gb_pipe.pkl','rb'))

@app.route('/')
def hello():
    return render_template('class.html')

@app.route('/mushroom_api',methods=['POST'])
def mushroom_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    input=(np.array(list(data.values())).reshape(1,-1))
    output=model.predict(input)[0]
    print(output)
    return jsonify(int(output))

@app.route('/mushroom',methods=['POST'])
def predict():
    data=[x for x in request.form.values()]
    print(data)
    input=(np.array(data).reshape(1,-1))
    print(input)
    output=model.predict(input)[0]
    res=''
    if output==1:
        res='POISONOUS'
    else:
        res='EDIBLE'
    return render_template('result.html',result='The Mushroom is {}'.format(res))

if __name__=='__main__':
    app.run(debug=True)