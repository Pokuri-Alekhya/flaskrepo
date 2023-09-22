pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out your Flask application source code from a Git repository
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build a Docker image for your Flask application
                script {
                    docker.build("myflaskimage:v1", "-f Dockerfile .")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                // Run a Docker container using the built image
                script {
                    docker.image("myflaskimage:v1").run("-d -p 80:5000 --name flaskcontainer")
                }
            }
        }

        stage('Testing') {
            steps {
                // Perform testing or other tasks
                echo 'Testing'
            }
        }
    }
}
