pipeline {
    agent any
    stages {
      stage('Build') {
        steps {
            sh 'make build'
        }
      }
      stage('Unit Test') {
        steps {
            sh 'make test'
        }
      }
    }
}