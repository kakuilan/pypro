#!/usr/bin/python3
# coding: utf-8
# flask启动例子
# export FLASK_APP=test125.py && flask run
# curl http://127.0.0.1:5000/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def powers(n=10):
  return ', '.join(str(2 **i) for i in range(n))
