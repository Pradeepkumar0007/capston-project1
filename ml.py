from flask import Flask ,render_template,request

import numpy as np


import pickle
model=Flask(__name__)


app= Flask(__name__)
@app.route("/")

def index():
    return render_template("index.html")


@app.route("/predict",methods=["POST"])

def predict_placement():
    temperature= float(request.form.get("temperature"))
    humidity = float(request.form.get("humidity"))
    ph = float(request.form.get("ph"))
    rainfall = float(request.form.get("rainfall"))


    result= model.predict(np.arrary([temperature,humidity,ph,rainfall]).reshape(1,3))

    return str(result)








if __name__ == "__main__":
    app.run(debug = True)