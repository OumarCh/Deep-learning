from flask import Flask, request, jsonify
import json
import numpy as np
import pickle

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/top_ten_gold')
def top_ten_gold():

    with open('workbook/json/top_ten_gold.json') as f:
        data = json.load(f)

    return data

@app.route('/top_ten_silver')
def top_ten_silver():
    with open('workbook/json/top_ten_silver.json') as f:
        data = json.load(f)

    return data

@app.route('/top_ten_bronze')
def top_ten_bronze():
    with open('workbook/json/top_ten_bronze.json') as f:
        data = json.load(f)

    return data

@app.route('/predict', methods = ['POST'])
def predict():

    data = request.get_json()
    medal = int(data.get('medal'))
    country_code = 1
    gold = int(data.get('gold'))
    silver = int(data.get('silver'))
    bronze = int(data.get('bronze'))
    score = int(data.get('score'))
    rank = int(data.get('score'))
    gdp = int(data.get('gdp'))
    particapant = int(data.get('number_of_participant'))

    to_predict_list = [medal, country_code, gold, silver, bronze, particapant, gdp, rank, score]

    print(np.array(to_predict_list).reshape(1, 9))

    model = pickle.load(open('workbook/summer-olympic-medals.pkl', 'rb'))
    print("after load")
    prediction = model.predict(np.array(to_predict_list).reshape(1, 9))

    print("prediction", prediction)
    # Take the first value of prediction
    cluster = int (prediction[0])

    return {"cluster": cluster}



if __name__ == "__main__":
    app.run(debug=True)