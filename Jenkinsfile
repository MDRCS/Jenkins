pipeline {
    agent any
    stages {
      stage('Build') {
        steps {
            echo "Building .."
            which make
            sh 'make build'

        }
      }
      stage('Unit Test') {
        steps {
            echo "Building .."
            sh 'make test'
        }
      }
    }
}