from flask import Flask, render_template
from flask import request, jsonify
from flask_pymongo import PyMongo
from bson import json_util
import json

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/travel_db"
mongo = PyMongo(app)

@app.route('/')
def get():
    return "Home"


@app.route('/get-information', methods = ['GET'])
def get_information():
    data = mongo.db.travel.find_one({'url_tour': 'https://dulichkhatvongviet.com/du-lich-trong-nuoc/ha-giang-bac-can-cao-bang-lang-son-bac-ninh/'})
    result = json.dumps(data, default=json_util.default)

    return render_template("index.html", data=result)



if __name__ == '__main__':
     app.run()