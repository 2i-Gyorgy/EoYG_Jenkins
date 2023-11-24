pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
    triggers {
        poolSCM 'H/5 * * * *'
    }
      }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                echo "doing build stuff..."
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing..."
                sh '''
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