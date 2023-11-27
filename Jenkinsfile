pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                bat '''
                dir
                cd myapp
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing..."
                bat '''
                cd myapp
                python hello.py
                python hello.py --name=Gyorgy
                '''
            }
        }
        stage('Test API') {
            steps {
                script {
                    // Run the Python script to make the API request
                    def apiResponse = bat(script: 'python apiTest.py', returnStdout: true).trim()

                    // Parse the status code from the API response
                    def statusCode = apiResponse.split("\n")[-1].trim().replaceAll("[^\\d]", '')

                    // Check if the status code is 200 (OK)
                    if (statusCode == "200") {
                        echo "API request successful"
                        // Add additional validation logic here if needed
                    } else {
                        error "API request failed with status code ${statusCode}"
                    }
                }
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                bat '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}