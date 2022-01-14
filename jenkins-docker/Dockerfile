FROM jenkinsci/blueocean

# create login for you and skip intial setup
#ENV JENKINS_USER admin
#ENV JENKINS_PASS admin

## Skip initial setup
#ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

ENV DOCKER_VERSION 20.10.7
ENV COMPOSE_VERSION 1.29.2

USER root
RUN apk add make \
  gcc \
  docker \
  py-pip \
  sudo \
  python3-dev \
  libffi-dev \
  openssl-dev \
  libc-dev \
  curl \
  docker-compose


# check installation
RUN docker-compose -version

COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/plugins.txt


# command to run this dockerfile -> sudo docker build -t custom-jenkins .

# After the image custom-jenkins is finished, run it with

# use user root other than default jenkins to avoid permission problem
# use docker on the host, because there is no docker daemon in a docker container
# sudo docker run --user root \
#		 -v /var/run/docker.sock:/var/run/docker.sock \
#		 -p 8080:8080 -p 50000:50000 custom-jenkins