pipeline {
    agent any
    stages {
      stage('Build') {
        steps {
            sh '''
                sudo apt-get install build-essential
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