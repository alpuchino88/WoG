pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t wow-app .'
            }
        }
        
        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:5000 -v $(pwd)/score.txt:/score.txt wow-app'
            }
        }
        
        stage('Test') {
            steps {
                sh 'python e2e.py http://localhost:8777'
            }
        }
        
        stage('Finalize') {
            steps {
                sh 'docker stop $(docker ps -q --filter ancestor=wow-app)'
                sh 'docker push alpuchino/wow-app'
            }
        }
    }
}

