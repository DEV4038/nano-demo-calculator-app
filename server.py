from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    val = request.json
    a = val['first']
    b = val['second']
    return jsonify({"result": a+b})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    val = request.json
    a = val['first']
    b = val['second']
    return jsonify({"result": a+b})

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
