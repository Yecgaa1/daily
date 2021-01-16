# code:utf-8
from flask import Flask, redirect, url_for, session, request, send_from_directory, abort, make_response
import json, os, hashlib, time, shutil

app = Flask(__name__)
Version = "0.0.1b"
app.config["SECRET_KEY"] = "renyizifuchuan"


@app.route('/ConnectTest', methods=['GET'])
def ConnectTest():
    return {
        "Version": Version
    }


if __name__ == '__main__':
    app.run(port=19150)
