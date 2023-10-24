from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route('/')
def indexx():
    return jsonify({
        "data":data,
        "meassage":"success"
    }),200

@app.route('/planet')
def planet():
    name=request.args.get("name")
    planet_data=next(item for item in data if item["name"]==name )
    return jsonify({
        "data": planet_data,
        "meassage":"success"
    }),200

if __name__ == "__main__":
    app.run()
