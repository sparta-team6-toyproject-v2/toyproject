from bson import json_util
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.rv3ttod.mongodb.net/test', tlsCAFile=ca)
db = client.hanghae_10_preliminary


@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/list')
# def list():
#     return render_template('2.html')


# @app.route('/travel', methods=["GET"])
# def list_get():
#     cities = ['루체른', '마드리드', '로마', '아테네', '파리',
#               '하와이', '칸쿤', '뉴욕', '몰디브', '발리', '보라카이', '세부', '다낭']
#     results = []
#     for city in cities:
#         result = db.travel.find_one({'city_kor': city}, {'_id': False})
#         results.append(result)
#     return jsonify(results)


# 태근님
@app.route('/tg')
def home_tg():
    return render_template('tg.html')


@app.route('/travel_tg', methods=["GET"])
def list_get():
    cities = ['루체른', '마드리드', '로마', '아테네', '파리',
              '하와이', '칸쿤', '뉴욕', '몰디브', '발리', '보라카이', '세부', '다낭']
    results = []
    for city in cities:
        result = db.travel.find_one({'city_kor': city}, {'_id': False})
        results.append(result)
    return jsonify(results)


# 승열님
@app.route('/sy')
def home_sy():
    return render_template('toy_sy.html')


@app.route("/travel", methods=["GET"])
def travel_get():
    travel_list = list(db.travel.find({}, {'_id': False}))

    return jsonify({'travel': travel_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)