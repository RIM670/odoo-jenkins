#!/bin/bash
set -e

echo "🚀 Déploiement des modules sur Odoo Prod..."


USER_PROD=rim
HOST_PROD=192.168.17.130  
DEST_PATH=/opt/odoo/custom_addons/



echo " Redémarrage du service Odoo sur la VM prod..."
ssh $USER_PROD@$HOST_PROD "sudo systemctl restart odoo17"

echo "Déploiement terminé avec succès."
ssh $USER_PROD@$HOST_PROD "echo '?? Service odoo17 status :' && systemctl status odoo17 | head -n 10"
ssh $USER_PROD@$HOST_PROD "ps -eo pid,lstart,cmd | grep odoo | grep -v grep"

