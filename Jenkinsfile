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
                script {
                    // Build the Docker image with the Flask application
                    sh 'sudo docker build -t myflaskimage:v1 .'
                }
            }
        }
        stage('Run Image') {
            steps {
                script {
                    // Run the Docker container and map port 8080 to 5000
                    sh 'sudo docker run -d --name flaskcontainer -p 80:80 myflaskimage:v1'
                }
            }
        }
      
    }
}
