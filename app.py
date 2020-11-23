from flask import Flask, request
app = Flask(__name__)


@app.route("/", methods=["GET", "POST", "OPTIONS"])
def hello():
    if request.method == "POST":
        print("触发器执行了")
    return "Hello World 😊"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')    