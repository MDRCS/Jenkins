pipeline {
    agent any
    stages {
      stage('Build') {
        steps {
            sh 'docker-compose build'
        }
      }
      stage('Unit Test') {
        steps {
            sh 'docker-compose run --rm app python -m pytest -v'
        }
      }
    }
}