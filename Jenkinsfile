pipeline {
    agent any
    environment {
        SCANNER_HOME = tool 'Sonar-scanner'
    }


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
            docker compose exec -T odoo odoo --test-enable -i car_agency --stop-after-init --database=odoo_test || true
        '''
    }
}
        stage('SonarQube Analysis') {
  steps {
    withSonarQubeEnv('sonar') {
      withCredentials([string(credentialsId: 'SONAR_TOKEN', variable: 'SONAR_TOKEN')]) {
        sh """
          echo Lancement de l’analyse SonarQube...
          export PATH=\$SCANNER_HOME/bin:\$PATH
          sonar-scanner \
            -Dsonar.projectKey=odoo-staging \
            -Dsonar.projectName=odoo-staging \
            -Dsonar.sources=addons \
            -Dsonar.exclusions=**/*.js,**/*.html \
            -Dsonar.host.url=http://192.168.1.168:9000 \
            -Dsonar.login=${SONAR_TOKEN}
        """
      }
    }
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
        stage('Trivy Security Scan') {
  steps {
    sh '''
      echo Running Trivy Scan...
      mkdir -p trivy-report
      curl -L https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/html.tpl -o html.tpl
      docker run --rm -v $(pwd):/project -w /project aquasec/trivy fs . \
        --format template --template "@html.tpl" -o trivy-report/trivy-report.html
    '''
  }
}
    }
     post {
always {
// Archive the Trivy report so it's downloadable from Jenkins UI
archiveArtifacts artifacts: 'trivy-report/*.html', fingerprint: true
}
}
}
