from flask import render_template, Response
from .request import RequestAPI
import json

def register_views(app):
    @app.route('/')
    def home():
        r = RequestAPI()
        return json.dumps(r.getPMData())