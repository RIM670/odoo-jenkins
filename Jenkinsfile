pipeline {
    agent any

    stages {
        stage('Déploiement Odoo Prod') {
            steps {
                sh './deploy-prod.sh'
            }
        }
        stage('Analyse SonarQube') {
  steps {
    withSonarQubeEnv('sonar') {
      withCredentials([string(credentialsId: 'SONAR_TOKEN', variable: 'SONAR_TOKEN')]) {
        sh '''
          echo "🔎 Lancement de l’analyse SonarQube..."
          sonar-scanner \
            -Dsonar.projectKey=odoo-prod \
            -Dsonar.projectName=odoo-prod \
            -Dsonar.sources=custom_addons \
            -Dsonar.exclusions=**/*.js,**/*.html \
            -Dsonar.host.url=$SONAR_HOST_URL \
            -Dsonar.login=$SONAR_TOKEN
        '''
      }
    }
  }}


    }
}
