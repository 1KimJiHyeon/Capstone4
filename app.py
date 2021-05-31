import flask
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

wind_spd = None
atm_pres = None
humid = None
temp = None
water_temp = None
max_wave_hsig_wave_h = None
avg_wave_h = None
wave_cycle = None

# 메인 페이지 라우팅
# 테스트 용도
@app.route("/")
def index():
    wind_spd = 1
    atm_pres = 2
    humid = 3
    temp = 4
    water_temp = 5
    max_wave_hsig_wave_h = 6

    test = wind_spd + atm_pres + humid + temp + water_temp + max_wave_hsig_wave_h

    return flask.render_template('index.html', prediction_ratio=test)

# 실시간 지도
@app.route('/map', methods=['GET'])
def mapGET():
    if request.method == 'GET':
        # 입력 받은 변수 값을 가지고 사고 위험 확률 예측
        prediction = (model.predict_proba([[0.09195619, 0.67504492, 0.75955954, 0.66476231, 0.56372769,
       0.17235857, 0.14059516, 0.05915105, 0.24763523]]))[0]

        # 예측 값을 1차원 배열로부터 확인 가능한 문자열로 변환
        prediction_ratio = '{:.2}%'.format(str(prediction[1]*100))

        # 결과 리턴
        return render_template('index.html', prediction_ratio=prediction_ratio)

# 실시간 위치_method GET
@app.route('/location', methods=['GET'])
def locationGET():
    if request.method == 'GET':

        # 입력 받은 변수 값을 가지고 사고 위험 확률 예측
        prediction = (model.predict_proba([[0.09195619, 0.67504492, 0.75955954, 0.66476231, 0.56372769,
       0.17235857, 0.14059516, 0.05915105, 0.24763523]]))[0]

        # 예측 값을 1차원 배열로부터 확인 가능한 문자열로 변환
        prediction_ratio = '{:.2}%'.format(str(prediction[1]*100))

        # 결과 리턴
        return render_template('index.html', prediction_ratio=prediction_ratio)

# 실시간 위치_method POST
@app.route('/location', methods=['POST'])
def locationPOST():
    if request.method == 'POST':
        # 입력 받은 변수 값을 가지고 사고 위험 확률 예측
        prediction = (model.predict_proba([[0.09195619, 0.67504492, 0.75955954, 0.66476231, 0.56372769,
       0.17235857, 0.14059516, 0.05915105, 0.24763523]]))[0]

        # 예측 값을 1차원 배열로부터 확인 가능한 문자열로 변환
        prediction_ratio = '{:.2}%'.format(str(prediction[1]*100))

        # 결과 리턴
        return render_template('index.html', prediction_ratio=prediction_ratio)

if __name__=="__main__":
    # 모델 로드
    # ml/model.py 선 실행 후 생성
    model = joblib.load('model/model.pkl')
    # Flask 서비스 스타트
    app.run(host='127.0.0.1', port=8080, debug=True)