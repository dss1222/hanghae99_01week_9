from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://54.180.148.164', 27017, username="test", password="test")
db = client.project #dtd

@app.route('/')
def home():
    # HTML 화면 보여주기
    # DB에 저장된 단어 찾아서 HTML에 나타내기
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        chickens = list(db.chicken.find({}))
        for chicken in chickens:
            # 치킨마다 해당 치킨을 좋아요 누른 수/해당 사용자가 누른 것이 맞는지(TorF) chickens 속에 추가
            chicken["_id"] = str(chicken["_id"])
            chicken["count_heart"] = db.likes.count_documents({"post_id": chicken["_id"], "type": "up"})
            chicken["heart_by_me"] = bool(db.likes.find_one({"post_id": chicken["_id"], "type": "up", "username": payload['id']}))
        # 좋아요 순서대로 정렬
        new_chickens = sorted(chickens, key = lambda chicken:chicken['heart_by_me'], reverse = True)

        return render_template('index.html', chickens=new_chickens) #정렬된 데이터를 index.html에 전달
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))




# # API 역할을 하는 부분 (ajax 사용시 구문)
# @app.route('/api/list', methods=['GET'])
# def show_Chicken():
#     chicken = list(db.chicken.find({},{'_id':False}).sort('like',-1))
#     return jsonify({'chickens': chicken})


# @app.route('/api/like', methods=['POST'])
# def like_Chicken():
#     name_receive = request.form['name_give']
#
#     target_chic = db.chicken.find_one({'name': name_receive})
#     current_like = target_chic['like']
#
#     new_like = current_like + 1
#
#     db.chicken.update_one({'name': name_receive}, {'$set': {'like': new_like}})
#
#     return jsonify({'msg': '좋아요 :)'})




@app.route('/detail/<keyword>')
def detail(keyword):
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        # API에서 단어 뜻 찾아서 결과 보내기
        chicken = db.chicken.find_one({"name": keyword}, {'_id': False})
        return render_template("detail.html", chicken=chicken, target=keyword)
    except jwt.ExpiredSignatureError:
         return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
         return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))





## 리뷰 작성 API




# 로그인 위한 추가 API
@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/user/<username>')
def user(username):
    # 각 사용자의 프로필과 글을 모아볼 수 있는 공간
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        status = (username == payload["id"])  # 내 프로필이면 True, 다른 사람 프로필 페이지면 False

        user_info = db.users.find_one({"username": username}, {"_id": False})
        return render_template('user.html', user_info=user_info, status=status)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


@app.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        return jsonify({'result': 'success','msg': '로그인 성공.', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,                               # 아이디
        "password": password_hash,                                  # 비밀번호
        "profile_name": username_receive,                           # 프로필 이름 기본값은 아이디
        "profile_pic": "",                                          # 프로필 사진 파일 이름
        "profile_pic_real": "profile_pics/profile_placeholder.png", # 프로필 사진 기본 이미지
        "profile_info": ""                                          # 프로필 한 마디
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})


@app.route('/update_profile', methods=['POST'])
def save_img():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # 프로필 업데이트
        return jsonify({"result": "success", 'msg': '프로필을 업데이트했습니다.'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


@app.route('/posting', methods=['POST'])
def posting():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # 포스팅하기
        user_info = db.users.find_one({"username": payload["id"]})
        star_receive = request.form["star_give"]
        comment_receive = request.form["comment_give"]
        date_receive = request.form["date_give"]
        target_receive= request.form["target_give"]

        doc = {
            "username": user_info["username"],
            "star": star_receive,
            "comment": comment_receive,
            "date": date_receive,
            "target": target_receive

        }
        db.posts.insert_one(doc)
        return jsonify({"result": "success", 'msg': '포스팅 성공'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))



@app.route("/get_posts/", methods=['GET'])
def get_posts():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # 포스팅 목록 받아오기
        target_receive=request.args.get("target_give")
        posts = list(db.posts.find({"target": target_receive}).sort("date", -1).limit(20))
        for post in posts:
            post["_id"] = str(post["_id"])

        return jsonify({"result": "success", "msg": "포스팅을 가져왔습니다.", "posts": posts})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))




@app.route('/update_like', methods=['POST'])
def update_like():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # 좋아요 수 변경

        user_info = db.users.find_one({"username": payload["id"]})
        post_id_receive = request.form["post_id_give"]
        type_receive = request.form["type_give"]
        action_receive = request.form["action_give"]
        doc = {
            "post_id": post_id_receive,
            "username": user_info["username"],
            "type": type_receive
        }
        if action_receive == "like":
            db.likes.insert_one(doc)
        else:
            db.likes.delete_one(doc)
        count = db.likes.count_documents({"post_id": post_id_receive, "type": type_receive})
        return jsonify({"result": "success", 'msg': 'updated', "count": count})

    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)








