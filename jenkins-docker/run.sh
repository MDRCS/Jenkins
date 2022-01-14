#!/bin/bash

# use user root other than default jenkins to avoid permission problem
# use docker on the host, because there is no docker daemon in a docker container
sudo docker run --user root \
		 -v /var/run/docker.sock:/var/run/docker.sock \
		 -p 8080:8080 -p 50000:50000 jenkins-blueocean