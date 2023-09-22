pipeline {
    agent any
    environment {
        PATH = "/usr/bin/docker"  // Update with the actual path to the Docker binary
    }
    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -t myflaskimage:v1 .'
            }
        }
        stage('Run Image') {
            steps {
                sh 'sudo docker run -d --name flaskcontainer myflaskimage:v1'
            }
            
        }
        stage('Testing') {
            steps {
               echo 'Testing'
            }
        }
    }
}
