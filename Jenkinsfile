pipeline {
    agent any
    stages {
      stage('Build') {
        steps {
            echo "Building .."
            // which make
            // sh 'make build'

        }
      }
      stage('Unit Test') {
        steps {
            echo "Testing .."
            sh 'python -m pytest -v'
            // sh 'make test'
        }
      }
    }
}