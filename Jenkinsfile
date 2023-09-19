pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Run Docker commands in WSL as the root user
                    bat "wsl sudo -S docker build -t my-docker-image:latest . <<< '123456789'"
                   
                }
            }
        }
            
        stage('Testing') {
            steps {
                echo 'Testing'
            }
        }
    }
}
