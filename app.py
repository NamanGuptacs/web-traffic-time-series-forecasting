from flask import Flask, jsonify, request
import numpy as np
import pickle
from keras.models import model_from_json
import pandas as pd
import datetime
import re

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
    client,access,language,predicted,time,page=final_object.predict(features[0],features[1])
    return flask.render_template('new.html',Client=client,Access=access,Language=language,predicted=predicted,time=time,Page=page)

if __name__ == '__main__':
    app.run(debug=True)
