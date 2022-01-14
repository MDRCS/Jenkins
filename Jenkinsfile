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