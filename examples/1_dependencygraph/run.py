#!/usr/bin/env python
from flask import Flask, jsonify
import multiapi

app = Flask(__name__)

@app.route('/<string:version>')
def multimodule(version):
        return jsonify(multiapi.get(version).execute())

