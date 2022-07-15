# docker-flask-locust
This project uses Locust to perform load testing on a simple Flask app

It simulates the application in production, and allows to check application performance under load

Create a virtualenv, then run the flask app. In another terminal, with the same virtualenv setup, run locust
```
# On the main terminal
python app.py

# On another terminal
locust
```

Locust runs on port 8089, so navigate to the browser and run the simulation.  
Specify the number of users to simulate, the spawn rate per second, and the host