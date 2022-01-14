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