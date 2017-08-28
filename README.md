# t2m
udp message server code test

To run it
* needs python 2.7 to run
* python t2m.py 0.0.0.0 1999

Vagrant-ized app:
* vagrant up && python test.py to test it
* logs to /vagrant/.t2m.log or /tmp/.t2m.log

Dockerized app:
* docker build -t test/python:centos7 . 
* python test_docker.py to test it
* logs to /tmp/.t2m.log (in the docker image filesystem) 


