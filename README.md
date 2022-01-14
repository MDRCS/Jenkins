# - Jenkins

- This Repo Provide ways of setting up Jenkins CI/CD pipelines and different Groovy Scripts.

### 1- Jenkins Blue Ocean Features:


    + Jenkins Blue Ocean comes with an embedded tool called the Visual Pipeline Editor. 
      This tool allows users to create and edit their pipeline.
      visually using a UI interface that’s accessible directly from the pipeline dashboard. 
      Also, the Visual Pipeline Editor saves your pipeline in code inside a file (Jenkinsfile), 
      following the Declarative Pipeline Syntax, directly to your source code repository.
      
    + The pipeline visualization allows users to diagnose pipeline failures with ease and speed. 
      When a pipeline fails, Blue Ocean tells you exactly where it has failed by pointing out the failed step. 
      Also, the pipeline logs are displayed individually for every stage and step of a pipeline, 
      so that users do not end up scrolling through a single huge log.

    + Blue Ocean also creates separate pages to view your testing results and built artifacts for every pipeline run.

### 2- Installing Jenkins Blue Ocean :

    + You can install Blue Ocean in the following two ways:
      1- As a suite of plugins on an existing Jenkins installation
      2- As part of Jenkins in Docker.
    
    + To run Jenkins from Docker Image :
    -> A docker image to give BlueOcean a try

    $ docker run -p 8080:8080 jenkinsci/blueocean
    1- note the admin password dumped on log
    2- open a browser on http://localhost:8080
    3- run the initial setup wizard. Choose "recommended plugins"
    4- browse to http://localhost:8080/blue

### 3- Visual Pipeline Editor :

    + When you create a pipeline in Blue Ocean, it automatically saves your pipeline design as pipeline code, 
     which is saved as a Jenkinsfile inside your source control repository.

### 4- getting started - Create CI Pipeline For Flask APP
    1- prepare A simple Flask app with Dockerfile, DockerCompose and test_app.py 
    2- Create a Dockerfile for Jenkins based on jenkins Blue Ocean Image (FROM jenkinsci/blueocean)
    3- Build Image using this command :
    $ sudo docker build -t jenkins-blueocean .
    4- Run Container using this command :
    $ sudo docker run --user root \
		 -v /var/run/docker.sock:/var/run/docker.sock \
		 -p 8080:8080 -p 50000:50000 jenkins-blueocean
    5- Prepare Makefile To run `Build` and `test` commands
    6- Prepare `Jenkinsfile` that run commands on every stage.
        ex: | 
            pipeline {
                agent any
                stages {
                  stage('Build') {
                    steps {
                        echo "Building .."
                        sh 'make build'
            
                    }
                  }
                  stage('Unit Test') {
                    steps {
                        echo "Testing .."
                        sh 'make test'
                    }
                  }
                }
            }
     
    * Congrats you have setup a CI pipeline               
    
