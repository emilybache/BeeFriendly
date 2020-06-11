from flask import Flask
from flask import request
import json
from tracing import init_tracer, flask_to_scope
from database import Flower
import opentracing
#from opentracing_instrumentation.client_hooks import install_all_patches
from flask_opentracing import FlaskTracer
from datetime import datetime

app = Flask('flower-service')
init_tracer('garden-service')
#install_all_patches()
flask_tracer = FlaskTracer(opentracing.tracer, True, app)


@app.route("/getFlower/<name>")
def get_flower_http(name):
    with flask_to_scope(flask_tracer, request) as scope:
        flower = Flower.get(name)
        if flower is None:
            flower = create_flower(name)

        result = {
            'name': flower.name,
            'flowering_months': flower.flowering_months.split(","),
            'description': flower.description,
        }

        opentracing.tracer.active_span.log_kv(result)
        return json.dumps(result)


def create_flower(name, now=None):
    flower = Flower()
    flower.name = name
    if not now:
        now = datetime.today()
    current_month = now.strftime('%B')
    flower.flowering_months = current_month.lower()
    return flower


if __name__ == "__main__":
    app.run(port=8081)
