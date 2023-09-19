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
                // Use the 'wsl' command to execute within WSL
                powershell 'wsl sudo docker build -t myflaskimage:v1 .'
            }
        }
        stage('Run Image') {
            steps {
                // Use the 'wsl' command to execute within WSL
                powershell 'wsl sudo docker run -d --name flaskcontainer myflaskimage:v1'
            }
        }
        stage('Testing') {
            steps {
               echo 'Testing'
            }
        }
    }
}
