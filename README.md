Bee Friendly
=============

This application uses a microservices architecture. You can use it to try out testing techniques.

Starting all the services
-------------------------

Use a different command window for each one.

## Front end

This is a Vue.js application.

	cd bee-friendly-ui
	npm run serve

## Garden Scorer

This is a python flask application:

	cd garden_scorer
	python3 -m flask run --port 3000

## Jaeger tracing

Download and run jaeger using docker:

	docker run -d --name jaeger \
	    -p 6831:6831/udp \
    	-p 16686:16686 \
    	-p 14268:14268 \
    	jaegertracing/all-in-one:1.6


## Testing it

When everything is started you should be able to open a browser on [http://localhost:8080](http://localhost:8080) and use the application. You should be able to see tracing in [jaeger](http://localhost:16686/).
