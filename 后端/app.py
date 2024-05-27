from flask import Flask, request
from static import CmdUtil, InfoGetter
from flask_cors import *

app = Flask(__name__)

CORS(app, supports_credentials=True, resources=r"/*")


@app.route('/')
def hello_world():  # put application's code here

    return 'hello'


@app.route('/connect', methods=['GET'])
def connect_and_work():
    hostname = request.args.get('hostname')
    num = request.args.get('num')
    CmdUtil.connect_and_work(hostname, num)

    return 'ing'


@app.route('/getInfo')
def get_info():
    data = ''
    with open('D:/TempSdnPlus/temp.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            data = data + line + '\n'

    return InfoGetter.getinfo(data)


if __name__ == '__main__':
    app.run()