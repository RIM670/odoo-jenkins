#!/bin/bash

JOB_NAME="odoo-prod-deploy"
JENKINS_URL="http://localhost:8080"
JENKINS_USER="admin"
JENKINS_API_TOKEN="ton_token_jenkins"
CONFIG_XML_PATH="./job-config/config.xml"

echo "[INFO] Création du job Jenkins : $JOB_NAME"

curl -X POST "${JENKINS_URL}/createItem?name=${JOB_NAME}" \
  --user "${JENKINS_USER}:${JENKINS_API_TOKEN}" \
  --header "Content-Type: application/xml" \
  --data-binary @"${CONFIG_XML_PATH}"

echo "[✅] Job créé. Vérifie dans Jenkins à ${JENKINS_URL}/job/${JOB_NAME}/"
