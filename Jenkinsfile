pipeline {

    agent any

    stages{
        triggers {
        githubPush()
        // Add more triggers for other events if needed
    }

 

 

   

        stage('Clone Repository') {

            steps {

                checkout scm

            }

        }

        stage('Build Image') {

            steps {

                sh 'sudo docker build -t imageflask1:latest .'

            }

        }

        stage('Run Image') {

            steps {

                sh 'sudo docker run -d --name containerflask -p 5000:5000 imageflask1:latest'

 

            }

 

        }

        stage('Testing') {

            steps {

               echo 'Testing'

            }

        }

    }

}
