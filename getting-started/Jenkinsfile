pipeline {
    agent any
        stages {
            stage('build') {
                steps {
                    "make build"
                }
            }
            stage('Unit Test') {
                steps {
                    "make test"
                }
            }
            stage('Publish') {
                steps {
                    "make release"
                }
            }
        }
}