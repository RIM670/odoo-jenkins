pipeline {
    agent any
     environment {
        SCANNER_HOME = tool 'Sonar-scanner'
    }

    stages {
        stage('Déploiement Odoo Prod') {
            steps {
                sh './deploy-prod.sh'
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
            -Dsonar.projectKey=odoo-prod \
            -Dsonar.projectName=odoo-prod \
            -Dsonar.sources=custom_addons \
            -Dsonar.exclusions=**/*.js,**/*.html \
            -Dsonar.host.url=http://192.168.17.128:9000 \
            -Dsonar.login=${SONAR_TOKEN}
        """
      }
    }
  }
}
stage('Security Scan with Bandit') {
  steps {
    sh '''
      echo Creating virtual environment for Bandit...
      python3 -m venv bandit-env
      . bandit-env/bin/activate
      echo  Installing Bandit...
      pip install --upgrade pip
      pip install bandit

      echo  Running Bandit on custom_addons/...
      bandit -r custom_addons/ -f html -o bandit-report.html || true

      deactivate
    '''
    // Optional/archive the report
    archiveArtifacts artifacts: 'bandit-report.html', allowEmptyArchive: true
  }
}
stage('Security Scan with Trivy') {
  steps {
    sh '''
      echo "  Running Trivy file system scan..."

      # Create directory for report
      mkdir -p trivy-report

   
  # Download Trivy HTML template
  curl -L https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/html.tpl -o html.tpl

  # Run Trivy and generate report
  docker run --rm -v $(pwd):/project -w /project aquasec/trivy fs . \
    --format template \
    --template "@html.tpl" \
    -o trivy-report/trivy-report.html
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

