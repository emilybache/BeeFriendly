from flask import Flask
from flask import request
import json
from .database import Flower
from lib.tracing import init_tracer, flask_to_scope
import opentracing
from opentracing.ext import tags
#from opentracing_instrumentation.client_hooks import install_all_patches
from flask_opentracing import FlaskTracer


app = Flask('flower-service')
init_tracer('flower-service')
#install_all_patches()
flask_tracer = FlaskTracer(opentracing.tracer, True, app)


@app.route("/getFlower/<name>")
def get_flower_http(name):
    with flask_to_scope(flask_tracer, request) as scope:
        flower = Flower.get(name)
        if flower is None:
            flower = Flower()
            flower.name = name
            flower.flowering_months = "june"

        result = {
            'name': flower.name,
            'flowering_months': flower.flowering_months.split(","),
            'description': flower.description,
        }

        opentracing.tracer.active_span.log_kv(result)
        return json.dumps(result)


if __name__ == "__main__":
    app.run(port=8081)
