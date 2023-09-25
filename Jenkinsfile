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

                sh 'sudo docker build -t imageflask:latest .'

            }

        }

        stage('Run Image') {

            steps {

                sh 'sudo docker run -d -p 6000:6000 imageflask:latest'

 

            }

 

        }

        stage('Testing') {

            steps {

               echo 'Testing'

            }

        }

    }

}
