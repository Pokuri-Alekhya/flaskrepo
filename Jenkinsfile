pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Build and Run Docker Image in PowerShell') {
            steps {
                script {
                    // Define the PowerShell script
                    def powerShellScript = """
                        # Build Docker image
                        docker build -t your-image-name .
                        
                        # Run Docker container
                        docker run -it your-image-name
                    """

                    // Execute the PowerShell script
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
