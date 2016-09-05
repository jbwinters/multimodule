#!/usr/bin/env python
from flask import Flask
import multiapi

app = Flask(__name__)

@app.route('/<string:version>')
def multimodule(version):
        return multiapi.get(version).execute()

