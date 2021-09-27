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

Then open a browser on localhost:8080
	

## Garden Scorer, Users etc

There are several python flask applications, named:

- flowers
- garden_scorer
- greeting
- newsletter
- users

For each one, named $SERVICE_NAME, start them in a separate window like this:

	cd $SERVICE_NAME/src
	python3 -m $SERVICE_NAME

## Jaeger tracing

Download and run jaeger using docker:

	docker run -d --name jaeger \
	    -p 6831:6831/udp \
    	-p 16686:16686 \
    	-p 14268:14268 \
    	jaegertracing/all-in-one:1.6

Alternatively, download jaeger binaries from [jaeger website](https://www.jaegertracing.io/download/). Unpack them and
link them under /usr/local/bin:

    sudo tar xvzf jaeger-1.26.0-linux-amd64.tar.gz  -C /opt/
    cd /usr/local/bin
    ln -s /opt/jaeger-1.26.0-linux-amd64/jaeger-all-in-one .
    
Start the jaeger-all-in-one binary then navigate to the [jaeger application](http://localhost:16686/) 

## databases

Install mysql. (The following instructions are for ec2 linux 2)

    sudo yum install mysql mariadb-server
    sudo systemctl start mariadb

Create the databases using the scripts in these services:

- flowers
- users

For each one:

    cd $SERVICE_NAME
    mysql -u root < database.sql
    

## Testing it

When everything is started you should be able to open a browser on [http://localhost:8080](http://localhost:8080) and use the application. 
You should be able to see tracing in [jaeger](http://localhost:16686/).

Before you can run texttest you will need to install [chrome driver](https://sites.google.com/chromium.org/driver/)
You will also need to install html2ascii from [uitext](https://github.com/texttest/uitext). Clone that repo then 
copy or softlink the script html2ascii.py under texttest/html2ascii/

Open texttest in the same folder as this README:

    texttest
    
Before the tests will pass you will need to start all the services.

