from flask import Flask, jsonify, request
import numpy as np
import pickle
from keras.models import model_from_json
import pandas as pd
import datetime
import re

from final_file import final
# https://www.tutorialspoint.com/flask
import flask
app = Flask(__name__)

final_object=final()
###################################################

###################################################


@app.route('/',methods=['GET'])
def home():
    return flask.render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    index=request.form.to_dict()['Enter_index']
    date=request.form.to_dict()['Enter_date']
    client,access,language,predicted,time=final_object.predict(index,date)
    return flask.render_template('new.html',Client=client,Access=access,Language=language,predicted=predicted,time=time)

if __name__ == '__main__':
    app.run(debug=True)
