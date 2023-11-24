pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                cmd_exec('cd myapp')
                cmd_exec('pip install -r requirements.txt')
            }
        }
        stage('Test') {
            steps {
                echo "Testing..."
                sh '''
                cd myapp
                python3 hello.py
                python3 hello.py --name=Gyorgy
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}