pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Build Image') {
            steps {
                sh docker build -t myflaskimage:v1 .'
            }
        }
        
    }
}
