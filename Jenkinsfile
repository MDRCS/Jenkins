pipeline {
    agent any
    stages {
      stage('Build') {
        steps {
            'make build'
        }
      }
      stage('Unit Test') {
        steps {
            'make test'
        }
      }
    }
}