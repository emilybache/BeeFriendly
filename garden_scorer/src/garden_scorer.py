import sys
import json
import requests
from flask import Flask, jsonify
from flask import request
from tracing import init_tracer, flask_to_scope, parse_baggage
import opentracing
from opentracing_instrumentation.client_hooks import install_all_patches
from flask_opentracing import FlaskTracer
from flask_cors import CORS, cross_origin

app = Flask('garden-scorer')
init_tracer('garden-scorer')
CORS(app)
install_all_patches()
flask_tracer = FlaskTracer(opentracing.tracer, True, app)


@app.route("/flower_scorer", methods=['GET', 'POST'])
@cross_origin()
def flower_scorer():
    with flask_to_scope(flask_tracer, request) as scope:
        #parse_baggage(request.headers, scope)
        if request.method == 'POST':
            params = json.loads(request.data)
            print(f"got form data {params.keys()}")
            garden_size = params['selected_garden_size']
            flowers = params['selected_flowers']
            score = calculate_score(garden_size, flowers)
            opentracing.tracer.active_span.set_tag('response', score)
            return jsonify({"score": score})


def fetch_flowering_months(flowers):
    flowering_months = set()
    for flower in flowers:
        json_object = _get("http://localhost:3005/getFlower/" + flower).json()
        flowering_months = flowering_months.union(json_object["flowering_months"])

    return flowering_months


def _get(url, params=None):
    r = requests.get(url, params=params)
    assert r.status_code == 200
    return r


def calculate_score(garden_size, flowers):
    with opentracing.tracer.start_active_span('calculate-score'):
        if len(flowers) == 0:
            return f"Our furry flying friends will be disappointed! You should plant some more flowers in your {garden_size} garden."

        if garden_size == "windowbox":
            return f"Top marks! Bees love your windowbox."
        else:
            flowering_months = fetch_flowering_months(flowers)
            if "july" not in flowering_months and "august" not in flowering_months:
                return f"Good work! Your garden would be even more friendly if you planted some flowers that bloom in " + get_months(flowering_months)
            else:
                return f"Top marks! Bees love your {garden_size} garden."



def get_months(flowering_months):
    return "July and August"

if __name__ == "__main__":
    app.run(port=3004)
