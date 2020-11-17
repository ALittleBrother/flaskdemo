from flask import Flask, request
app = Flask(__name__)


@app.route("/", methods=["GET", "POST", "OPTIONS"])
def hello():
    if request.method == "POST":
        print("触发器执行了")
    return "欢迎使用 CODING 代码模板, 更新代码尝试自动构建, 再次更新, 试下 ssh 配置是否生效"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')    