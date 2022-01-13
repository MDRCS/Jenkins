pipeline {
    agent any
    stages {
      stage('Build') {
        steps {
            sh 'build' // make build
        }
      }
      stage('Unit Test') {
        steps {
            sh 'test' // make test
        }
      }
    }
}