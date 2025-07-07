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
                sh '''
                    echo "🔎 Lancement de l’analyse SonarQube..."

                    # Ajoute le dossier sonar-scanner à ton PATH si nécessaire :
                    export PATH=$PATH:/opt/sonar-scanner/bin

                    sonar-scanner \
                      -Dsonar.projectKey=odoo-prod \
                      -Dsonar.projectName=odoo-prod \
                      -Dsonar.sources=custom_addons \
                      -Dsonar.exclusions=**/*.js,**/*.html \
                      -Dsonar.host.url=http://192.168.17.128:9000 \
                      -Dsonar.login=$SONAR_TOKEN
                '''
            }
        }
    }
}



    }
}
