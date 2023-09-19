pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Build and Run Docker Image in WSL') {
            steps {
                script {
                    // Define the PowerShell script
                    def powerShellScript = """

                        wsl

 

                        

                    """

 

                    sh "echo 'root' | wsl"

 

                       
                     sh "docker build -t your-image-name ."
                     sh "docker run -it your-image-name"
                    bat(script: powerShellScript, returnStatus: true)
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
