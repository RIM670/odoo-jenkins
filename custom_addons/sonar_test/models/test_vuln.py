from odoo import models, fields, api
import os

class SonarTest(models.Model):
    _name = 'sonar.test'
    _description = 'Test de sécurité SonarQube'

    name = fields.Char("Nom")

    @api.model
    def read_sensitive_file(self):
        # ?? Vulnérabilité : accès à un fichier systèm
        with open('/etc/passwd', 'r') as f:
            return f.read()

    @api.model
    def insecure_eval(self, code):
        # ?? Vulnérabilité : exécution dynamique non sécurisée
        return eval(code)

    @api.model
    def command_injection(self, user_input):
        # ?? Vulnérabilité : injection de commande shell
        return os.system(f"ping -c 1 {user_input}")
