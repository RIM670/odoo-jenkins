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
                sh 'docker compose down || true'
                sh 'docker compose up -d'
            }
        }
       
}
        

        stage('Initialize Odoo DB') {
    steps {
        sh '''
            echo "Initializing Odoo DB..."
            docker compose exec -T odoo odoo -i base --database=odoo --without-demo=all --stop-after-init || true
        '''
    }
}
        stage('Run Unit Tests') {
    steps {
        sh '''
            echo "Running tests..."
            docker compose exec -T odoo odoo --test-enable -i my_module --stop-after-init --database=odoo_test || true
        '''
    }
}
        stage('Owasp Scan') {
            steps {
                dependencyCheck additionalArguments: ' --scan ./ ', odcInstallation: 'DC'
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
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
