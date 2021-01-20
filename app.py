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
class Form(FlaskForm):
    index = IntegerField('Enter_index', validators=[InputRequired('Enter a correct index'),NumberRange(0,9999)])

@app.route('/',methods=['GET'])
def home():
    return flask.render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    #features = [x for x in request.form.values()]
    if request.method == "POST":
        form = Form()  # will register fields called 'username' and 'email'.
        if form.validate_on_submit():
            client,access,language,predicted,time,page=final_object.predict(index,features[1])
            return flask.render_template('new.html',Client=client,Access=access,Language=language,predicted=predicted,time=time,Page=page)

if __name__ == '__main__':
    app.run(debug=True)
