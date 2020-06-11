import logging
import opentracing
from jaeger_client import Config


def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
            'reporter_batch_size': 1,
        },
        service_name=service,
    )

    # this call sets global variable opentracing.tracer
    config.initialize_tracer()


def flask_to_scope(flask_tracer, request):
    return opentracing.tracer.scope_manager.activate(
        flask_tracer.get_span(request),
        False,
    )


def parse_baggage(headers, scope):
    baggage = headers.get("jaeger-baggage")
    print(f"found baggage: {baggage}")

    if not baggage:
        return

    fields_as_dict = dict([f.split("=") for f in (baggage.split(","))])
    if "session" in fields_as_dict.keys():
        sessionId = fields_as_dict.get("session")
        scope.span.set_tag("garden-session", sessionId)
        #print(f"set session {sessionId}")
    if "request" in fields_as_dict.keys():
        requestId = fields_as_dict.get("request")
        scope.span.set_tag("quizz-request", requestId)
        #print(f"set request {requestId}")
