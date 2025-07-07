#!/bin/bash

set -e

JENKINS_URL="http://localhost:8080"
JENKINS_USER="rim"
JENKINS_PASSWORD="0000" 



# Étape 1 - Télécharger jenkins-cli.jar depuis Jenkins en local
echo " Téléchargement de jenkins-cli.jar depuis $JENKINS_URL"
wget -q $JENKINS_URL/jnlpJars/jenkins-cli.jar

# Étape 2 - Créer le job dans Jenkins
echo " Création du job 'odoo-pipeline' dans Jenkins..."

java -jar jenkins-cli.jar -s $JENKINS_URL \
  -auth $JENKINS_USER:$JENKINS_PASSWORD \
  update-job odoo-pipeline-prod < ./job-config/config.xml

echo " Pipeline Jenkins créée avec succès !"

