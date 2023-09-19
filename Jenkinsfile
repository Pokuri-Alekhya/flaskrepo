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
                        123456789

 

                       
 

                        # You are now inside the WSL environment, run Docker commands
                        docker build -t your-image-name .
                        docker run -it your-image-name
                    """

 

                    // Execute the PowerShell script in PowerShell
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
