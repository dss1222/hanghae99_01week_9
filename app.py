from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.project #dtd


# HTML 화면 보여주기
@app.route('/')
def main():
    #DB에 저장된 단어 찾아서 HTML에 나타내기
    chickens = list(db.chicken.find({}, {'_id':False}).sort('like',-1))
    return render_template('index.html', chickens=chickens)



# # API 역할을 하는 부분 (ajax 사용시 구문)
# @app.route('/api/list', methods=['GET'])
# def show_Chicken():
#     chicken = list(db.chicken.find({},{'_id':False}).sort('like',-1))
#     return jsonify({'chickens': chicken})


@app.route('/api/like', methods=['POST'])
def like_Chicken():
    name_receive = request.form['name_give']

    target_chic = db.chicken.find_one({'name': name_receive})
    current_like = target_chic['like']

    new_like = current_like + 1

    db.chicken.update_one({'name': name_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': '좋아요 :)'})


@app.route('/api/delete', methods=['POST'])
def delete_star():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'delete 연결되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)