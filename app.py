from flask import Flask, jsonify, request
import numpy as np
import pickle
from keras.models import model_from_json
import pandas as pd
import datetime
import re
from flask_wtf import FlaskForm
from wtforms.validators import NumberRange, InputRequired
from wtforms import TextField,IntegerField
from final_file import final

import flask
app = Flask(__name__)

final_object=final()

@app.route('/',methods=['GET'])
def home():
    return flask.render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    features = [x for x in request.form.values()]
    flag_ind = 0
    flag_date = 0
    if feature[0].isdigit() == True:
        flag_ind=1
    if datetime.datetime.strptime(features[1], '%Y-%m-%d')==True:
        flag_date=1
    if flag_ind==1 && flag_date==0:
        return flask.render_template('index.html',error_index="Enter a Correct Index between 0-9999")
    if flag_ind==0 && flag_date==1:
        return flask.render_template('index.html',error_date="Enter a Correct Date between 2015-07-06-2017-09-10")
    if flag_ind==0 && flag_date==0:     
        if 0 <= int(features[0]) <= 9999 and features[1] in pd.date_range(start='2015-07-06', end='2017-09-10'):
            client,access,language,predicted,time,page=final_object.predict(features[0],features[1])
            return flask.render_template('new.html',Client=client,Access=access,Language=language,predicted=predicted,time=time,Page=page)
        else:
            return flask.render_template('index.html',error_date="Enter a Correct Date between 2015-07-06-2017-09-10",error_index="Enter a Correct Index between 0-9999")
        
if __name__ == '__main__':
    app.run(debug=True)
