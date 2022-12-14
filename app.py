from bson import json_util
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.rv3ttod.mongodb.net/test', tlsCAFile=ca)
db = client.hanghae_10_preliminary


@app.route('/')
def home():
    return render_template('index.html')


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
@app.route('/루체른')
def home_lucerne():
    return render_template('toy_sy_루체른.html')


@app.route('/마드리드')
def home_madrid():
    return render_template('toy_sy_마드리드.html')


@app.route('/로마')
def home_rome():
    return render_template('toy_sy_로마.html')


@app.route('/아테네')
def home_athens():
    return render_template('toy_sy_아테네.html')


@app.route('/파리')
def home_paris():
    return render_template('toy_sy_파리.html')


@app.route('/하와이')
def home_hawaii():
    return render_template('toy_sy_하와이.html')


@app.route('/칸쿤')
def home_cancun():
    return render_template('toy_sy_칸쿤.html')


@app.route('/뉴욕')
def home_newyork():
    return render_template('toy_sy_뉴욕.html')


@app.route('/몰디브')
def home_maldives():
    return render_template('toy_sy_몰디브.html')


@app.route('/발리')
def home_bali():
    return render_template('toy_sy_발리.html')


@app.route('/보라카이')
def home_boracay():
    return render_template('toy_sy_보라카이.html')


@app.route('/세부')
def home_cebu():
    return render_template('toy_sy_세부.html')


@app.route('/다낭')
def home_danang():
    return render_template('toy_sy_다낭.html')



@app.route("/travel", methods=["GET"])
def travel_get():
    travel_list = list(db.travel.find({}, {'_id': False}))

    return jsonify({'travel': travel_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
