pipeline {
    agent any

    stages {
        stage('Clone staging') {
            steps {
                git branch: 'staging', url: 'https://github.com/RIM670/odoo-jenkins.git'
            }
        }

        stage('Start Docker Compose') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker-compose up -d'
            }
        }

        stage('Health Check') {
            steps {
                sh 'sleep 10'
                sh 'curl -f http://localhost:8069 || exit 1'
            }
        }
    }
}
