import sys
import json
import requests
from flask import Flask, jsonify
from flask import request
from tracing import init_tracer, flask_to_scope
import opentracing
from opentracing.ext import tags
#from opentracing_instrumentation.client_hooks import install_all_patches
from flask_opentracing import FlaskTracer
from flask_cors import CORS, cross_origin

app = Flask('garden-scorer')
init_tracer('garden-scorer')
CORS(app)
#install_all_patches()
flask_tracer = FlaskTracer(opentracing.tracer, True, app)


@app.route("/flower_scorer", methods=['GET', 'POST'])
@cross_origin()
def flower_scorer():
    with flask_to_scope(flask_tracer, request) as scope:
        if request.method == 'POST':
            print(f"got request with data keys {request.data}")
            params = json.loads(request.data)
            garden_size = params['selected_garden_size']
            score = calculate_score(garden_size)
            opentracing.tracer.active_span.set_tag('response', score)
            return jsonify({"score": score})



def calculate_score(garden_size):
    return f"Top marks! Bees love your {garden_size} garden."


def get_person(name):
    with opentracing.tracer.start_active_span(
        'get-person',
    ) as scope:
        url = 'http://localhost:8081/getPerson/%s' % name
        res = _get(url)
        person = json.loads(res)
        scope.span.log_kv({
            'name': person['name'],
            'title': person['title'],
            'description': person['description'],
        })
        return person


def format_greeting(person):
    with opentracing.tracer.start_active_span(
        'format-greeting',
    ):
        url = 'http://localhost:8082/formatGreeting'
        return _get(url, params=person)


def _get(url, params=None):
    r = requests.get(url, params=params)
    assert r.status_code == 200
    return r.text


if __name__ == "__main__":
    app.run(port=8080)
