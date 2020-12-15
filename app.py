from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'my_database'
app.config["MONGO_URI"] = "mongodb://localhost:27017/my_database"

mongo = PyMongo(app)

@app.route('/polution', methods=['GET'])
def get_all_data():
    data = mongo.db.air_polution
    output = []
    for s in data.find():
        output.append({'datetime' : s['datetime'], 
                        'address' : s['address'],
                        'pm2.5' : s['pm25'],
                        'pm10' : s['pm10'],
                        'polution_lv' : s['polution_lv']
                        })
    return jsonify({'result' : output})

@app.route('/polution/last_update', methods=['GET'])
def get_polution_last_update():
    data = mongo.db.air_polution
    output = []
    for s in data.find().sort('_id',-1).limit(1):
        output.append({'datetime' : s['datetime'], 
                        'address' : s['address'],
                        'pm2.5' : s['pm25'],
                        'pm10' : s['pm10'],
                        'polution_lv' : s['polution_lv']
                        })
    return jsonify({'result' : output})

@app.route('/polution/datetime', methods=['GET'])
def get_polution_dt():
    data = mongo.db.air_polution
    output = []
    for s in data.find().sort('_id',-1).limit(1):
        output.append({'Datetime' : s['datetime']
                        })
    return jsonify({'result' : output})

@app.route('/polution/lv', methods=['GET'])
def get_polution_lv():
    data = mongo.db.air_polution
    output = []
    for s in data.find().sort('_id',-1).limit(1):
        output.append({'polution_lv' : s['polution_lv']
                        })
    return jsonify({'result' : output})

@app.route('/polution/location', methods=['GET'])
def get_polution_address():
    data = mongo.db.air_polution
    output = []
    for s in data.find().sort('_id',-1).limit(1):
        output.append({'location' : s['address']
                        })
    return jsonify({'result' : output})

@app.route('/polution/pm2.5', methods=['GET'])
def get_polution_pm25():
    data = mongo.db.air_polution
    output = []
    for s in data.find().sort('_id',-1).limit(1):
        output.append({'pm2.5' : s['pm25']
                        })
    return jsonify({'result' : output})

@app.route('/polution/pm10', methods=['GET'])
def get_polution_pm10():
    data = mongo.db.air_polution
    output = []
    for s in data.find().sort('_id',-1).limit(1):
        output.append({'pm10' : s['pm10']
                        })
    return jsonify({'result' : output})
  
if __name__ == '__main__':
    app.run(debug=True,port=8000)