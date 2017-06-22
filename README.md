# Sample Python Flask application in docker for demos

This example uses nginx and uwsgi to run the flask app, a preferred configuration for more robust apps

The source Docker image this file pulls from is defined [here](https://github.com/tiangolo/uwsgi-nginx-docker/blob/master/python2.7/Dockerfile)  



Build

```
$ docker build -t my_flask_app .
```

Run

```
$ docker run -it --rm -p 80:80 my_flask_app
```