#!/bin/bash
set -e

echo "🚀 Déploiement des modules sur Odoo Prod..."

# Variables à adapter
USER_PROD=rim
HOST_PROD=192.168.17.130  # IP de ta VM Odoo installée manuellement
DEST_PATH=/opt/odoo/custom_addons/

# Copier les modules personnalisés
#echo "📦 Copie des modules personnalisés vers la VM prod..."
#scp -r custom_addons/* $USER_PROD@$HOST_PROD:$DEST_PATH

# Copier le fichier de config si nécessaire (facultatif)
# scp config/odoo.conf $USER_PROD@$HOST_PROD:/etc/odoo/odoo.conf

# Redémarrer le service Odoo
echo "♻️ Redémarrage du service Odoo sur la VM prod..."
ssh $USER_PROD@$HOST_PROD "sudo systemctl restart odoo17"

echo "✅ Déploiement terminé avec succès."
ssh $USER_PROD@$HOST_PROD "echo '?? Service odoo17 status :' && systemctl status odoo17 | head -n 10"
ssh $USER_PROD@$HOST_PROD "ps -eo pid,lstart,cmd | grep odoo | grep -v grep"

