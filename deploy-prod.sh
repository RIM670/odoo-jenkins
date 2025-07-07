#!/bin/bash
set -e

echo "🚀 Déploiement des modules sur Odoo Prod..."

# Variables à adapter
USER_PROD=odoo
HOST_PROD=192.168.17.130  # IP de ta VM Odoo installée manuellement
DEST_PATH=/opt/odoo/custom_addons/

# Copier les modules personnalisés
#echo "📦 Copie des modules personnalisés vers la VM prod..."
#scp -r custom_addons/* $USER_PROD@$HOST_PROD:$DEST_PATH

# Copier le fichier de config si nécessaire (facultatif)
# scp config/odoo.conf $USER_PROD@$HOST_PROD:/etc/odoo/odoo.conf

# Redémarrer le service Odoo
echo "♻️ Redémarrage du service Odoo sur la VM prod..."
ssh $USER_PROD@$HOST_PROD "sudo systemctl restart odoo"

echo "✅ Déploiement terminé avec succès."
