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

client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://54.180.148.164', 27017, username="test", password="test")
db = client.project  # dtd


@app.route('/')
def home():
    # HTML 화면 보여주기
    # DB에 저장된 단어 찾아서 HTML에 나타내기

    #해당 이용자 컴퓨터에 저장된 쿠키에서 토큰 가져오기
    token_receive = request.cookies.get('mytoken')
    try:
        # 로그인된 jwt 토큰 디코드하여 payload 설정
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # chicken db에서 모든 치킨 정보 불러오기
        chickens = list(db.chicken.find({}))
        for chicken in chickens:
            # 치킨마다 해당 치킨을 좋아요 누른 수/해당 사용자가 누른 것이 맞는지(TorF) chickens 속에 추가
            chicken["_id"] = str(chicken["_id"])
            chicken["count_heart"] = db.likes.count_documents({"post_id": chicken["_id"], "type": "up"})
            chicken["heart_by_me"] = bool(db.likes.find_one({"post_id": chicken["_id"], "type": "up", "username": payload['id']}))
        # 좋아요 누른 수 순으로 내림차순 정렬
        new_chickens = sorted(chickens, key=lambda chicken: chicken['count_heart'], reverse=True)
        # 정렬된 데이터를 index.html으로 전달
        return render_template('index.html', chickens=new_chickens)
    # 토큰 로그인 시간 만료 시, msg와 함께 /login 페이지로 돌아감
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    # 토큰 디코딩 오류 발생 시
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/detail/<keyword>') #치킨 이름을 <keyword>로 받음
def detail(keyword):
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        # API에서 해당 치킨 데이터 찾아서 결과 보내기
        chicken = db.chicken.find_one({"name": keyword}, {'_id': False})
        # 해당 chicken 데이터와 상세페이지 리뷰 포스팅을 위해 keyword(치킨 이름)도 detail.html으로 보내기기
        return render_template("detail.html", chicken=chicken, target=keyword)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


# 회원가입 API
@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    # id, pw 받아서, mongoDB에 저장하기
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()

    doc = {
        "username": username_receive,  # 아이디
        "password": password_hash,  # 비밀번호
        "profile_name": username_receive,  # 프로필 이름 기본값은 아이디
        "profile_pic_real": "profile_pics/profile_placeholder.png"  # 프로필 사진 기본 이미지
    }
    db.users.insert_one(doc)  # users db에 위 내용을 집어 넣음

    return jsonify({'result': 'success'})


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


# 로그인 API
@app.route('/sign_in', methods=['POST'])
def sign_in():
    # username과 password 받아오기
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    # password 해시함수 (암호화)
    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    # 해당 사용자가 users db에서 username과 password가 있는지 확인
    # 있으면 JWT 토큰 만들어서 발급 / exp에 만료시간을 넣어주기
    if result is not None:
        payload = {
            'id': username_receive,  # id에 username을 받아옴
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        return jsonify({'result': 'success', 'msg': '로그인 성공.', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})



@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():  # 아이디 중복확인
    username_receive = request.form['username_give']  # check_dup()로부터 username을 받아옴
    exists = bool(db.users.find_one({"username": username_receive}))  # username이 중복되면면 true 중복이아니면 false
    return jsonify({'result': 'success', 'exists': exists})  # exist라는 값을 클라이언트로 보내줌 true인지 false인지


@app.route('/posting', methods=['POST'])
def posting():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # 포스팅하기
        user_info = db.users.find_one({"username": payload["id"]})  # id를 받아오기
        star_receive = request.form["star_give"]  # star(이모지)를 받아오기
        comment_receive = request.form["comment_give"]  # comment를 받아오기
        date_receive = request.form["date_give"]  # date를 받아오기
        target_receive = request.form["target_give"]  # 해당 페이지 치킨 이름 받아오기

        doc = {
            "username": user_info["username"],
            "star": star_receive,
            "comment": comment_receive,
            "date": date_receive,
            "target": target_receive
        }
        db.posts.insert_one(doc)  # posts라는 db로 저장
        return jsonify({"result": "success", 'msg': '포스팅 성공'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


@app.route("/get_posts/", methods=['GET'])
def get_posts():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # 포스팅 목록 받아오기
        target_receive = request.args.get("target_give")  # 해당 페이지 치킨 이름(target)을 받아옴
        # db에서 해당 페이지의 리뷰를 찾아 시간순, 20개까지 보여줌
        posts = list(db.posts.find({"target": target_receive}).sort("date", -1).limit(20))
        # "_id"를 문자열로 바꿔야 넘길 수 있음
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
        # 좋아요 누른 사용자의 정보 받기
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
            # 좋아요를 누른 것이면 likes db에 저장하기 (저장되면 좋아요 수에 count)
            db.likes.insert_one(doc)
        else:
            # 이미 눌렀던 좋아요일 때, likes db에서 삭제하기 (좋아요 취소)
            db.likes.delete_one(doc)
        # 같은 post_id(치킨 id)를 count하면 좋아요 수가 나옴
        count = db.likes.count_documents({"post_id": post_id_receive, "type": type_receive})
        return jsonify({"result": "success", 'msg': 'updated', "count": count})

    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))

# 리뷰 삭제 API
@app.route('/delete', methods=['POST'])
def delete_star():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        comment_receive = request.form['comment_give']  # name을 받아옴
        db.posts.delete_one({'comment': comment_receive})  # 받아온 comment 값과 일치하는 딕셔너리 삭제
        return jsonify({'msg': '삭제되었습니다.!'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
