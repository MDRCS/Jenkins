pipeline {
    agent any
    stages {
      stage('Build') {
        steps {
            sh '''
                apt-get install build-essential
                echo $PATH
                echo "building .."
                make build
               '''
        }
      }
      stage('Unit Test') {
        steps {
            sh '''
               echo "testing .."
               make test
               '''
        }
      }
    }
}