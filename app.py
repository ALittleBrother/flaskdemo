from flask import Flask, request
import json
app = Flask(__name__)

"""
POST /payload HTTP/1.1

Content-Type: application/json
Request URL: https://cs.console.aliyun.com/hook/trigger?triggerUrl=YzRmMWE5YzM2ZjMzYzQ0NmFiMGYzNWJlMmM2MjM2NzIyfGV4cHJlc3N8cmVkZXBsb3l8MThlMmllY2drdXYyZXw=&secret=365a4a664b45615438716a487a75695a7ac48329224b35b073c2197374e7d62a
Request method: POST

{
    "push_data": {
        "digest": "sha256:457f4aa83fc9a6663ab9d1b0a6e2dce25a12a943ed5bf2c1747c58d48bbb4917", 
        "pushed_at": "2016-11-29 12:25:46", 
        "tag": "latest"
    }, 
    "repository": {
        "date_created": "2016-10-28 21:31:42", 
        "name": "repoTest", 
        "namespace": "namespace", 
        "region": "cn-hangzhou", 
        "repo_authentication_type": "NO_CERTIFIED", 
        "repo_full_name": "namespace/repoTest", 
        "repo_origin_type": "NO_CERTIFIED", 
        "repo_type": "PUBLIC"
    }
}
"""


@app.route("/", methods=["GET", "POST", "OPTIONS"])
def hello():
    if request.method == "POST":
        data = request.data
        data = bytes.decode(data, "utf-8")
        if data:
            format_data = json.loads(data, encoding="utf-8")
            print(format_data)
        print("触发器执行了")
    return "Hello World, Nice to meet you! 😊"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
