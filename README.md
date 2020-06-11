Bee Friendly
=============

This application uses a microservices architecture. You can use it to try out testing techniques.

Starting all the services
-------------------------

Use a different command window for each one.

## Front end

This is a Vue.js application. First install the needed npm modules:

	cd bee-friendly-ui
	npm install 
	
Then start the server:

	npm run serve
	

## Garden Scorer

This is a python flask application:

	cd garden_scorer
	export FLASK_APP=src/scorer.py
	python3 -m flask run --port 3000

## Jaeger tracing

Download and run jaeger using docker:

	docker run -d --name jaeger \
	    -p 6831:6831/udp \
    	-p 16686:16686 \
    	-p 14268:14268 \
    	jaegertracing/all-in-one:1.6

Alternatively, download jaeger binaries from [jaeger website](https://www.jaegertracing.io/download/).
Start the jaeger-all-in-one binary.

## Flower Service

Install mysql, and create the database 'flowerdb' using the script flower_service/database.sql. (The following instructions are for ec2 linux 2)

    sudo yum install mysql mariadb-server
    sudo systemctl start mariadb
    mysql -u root < database.sql
    
Start the python flask application:

	cd flower_service
	export FLASK_APP=src/flower_service.py
	python3 -m flask run --port 3001


## Testing it

When everything is started you should be able to open a browser on [http://localhost:8080](http://localhost:8080) and use the application. You should be able to see tracing in [jaeger](http://localhost:16686/).

## 3rd party software

This program bundles the tool 'html2ascii' which is released under the GNU Lesser General Public License v2.1. For more information see [the github page](https://github.com/texttest/html2ascii). It is included under the 'texttest' subdirectory.

