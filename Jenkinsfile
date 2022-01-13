pipeline {
    agent any
    stages {
      stage('Build') {
        steps {
            sh '''
                which make
                make build
               '''
        }
      }
      stage('Unit Test') {
        steps {
            sh 'make test'
        }
      }
    }
}