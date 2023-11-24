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