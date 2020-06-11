import sys
import json
import requests
from flask import Flask, jsonify
from flask import request
from tracing import init_tracer, flask_to_scope
import opentracing
from opentracing.ext import tags
from opentracing_instrumentation.client_hooks import install_all_patches
from flask_opentracing import FlaskTracer
from flask_cors import CORS, cross_origin


app = Flask('garden-quizz')
init_tracer('garden-quizz')
install_all_patches()
CORS(app)
flask_tracer = FlaskTracer(opentracing.tracer, True, app)


@app.route("/quizz", methods=['GET', 'POST'])
@cross_origin()
def garden_quizz():
    with flask_to_scope(flask_tracer, request) as scope:
        if request.method == 'POST':
            params = json.loads(request.data)
            garden_size = params['selected_garden_size']
            flowers = params['selected_flowers']
            score = calculate_score(garden_size, flowers)
            opentracing.tracer.active_span.set_tag('response', score)
            return jsonify({"score": score})


def calculate_score(garden_size, flowers):
    with opentracing.tracer.start_active_span(
        'calculate-score',
    ):
        url = 'http://localhost:3004/flower_scorer'
        data = {"selected_garden_size": garden_size,
                    "selected_flowers": flowers}
        print("posting data", data)
        response = _post(url, data)
        print("got response ", response)
        return response.json()


def _post(url, data):
    r = requests.post(url, data=data)
    #assert r.status_code == 200
    return r


if __name__ == "__main__":
    app.run(port=3006)
