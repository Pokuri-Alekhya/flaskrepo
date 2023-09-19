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

 

                    bat "echo '123456789' | wsl"

 

                       
                     bat "docker build -t your-image-name ."
                     bat "docker run -it your-image-name"
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
