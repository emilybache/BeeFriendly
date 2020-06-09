import sys
import json
import requests
from flask import Flask, jsonify
from flask import request
from tracing import init_tracer, flask_to_scope, parse_baggage
import opentracing
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
        parse_baggage(request.headers, scope)
        if request.method == 'POST':
            params = json.loads(request.data)
            garden_size = params['selected_garden_size']
            score = calculate_score(garden_size)
            opentracing.tracer.active_span.set_tag('response', score)
            return jsonify({"score": score})



def calculate_score(garden_size):
    return f"Top marks! Bees love your {garden_size} garden."


if __name__ == "__main__":
    app.run(port=8080)
