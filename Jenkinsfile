pipeline {
    agent any
    stages {
      stage('Build') {
        steps {
            sh '''
                echo $PATHs
                echo "building .."
                ./make build
               '''
        }
      }
      stage('Unit Test') {
        steps {
            sh '''
               echo "testing .."
               ./make test
               '''
        }
      }
    }
}