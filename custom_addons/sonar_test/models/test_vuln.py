from odoo import models, fields, api
import os

class SonarTest(models.Model):
    _name = 'sonar.test'
    _description = 'Test de s�curit� SonarQube'

    name = fields.Char("Nom")

    @api.model
    def read_sensitive_file(self):
        # ?? Vuln�rabilit� : acc�s � un fichier syst�me
        with open('/etc/passwd', 'r') as f:
            return f.read()

    @api.model
    def insecure_eval(self, code):
        # ?? Vuln�rabilit� : ex�cution dynamique non s�curis�e
        return eval(code)

    @api.model
    def command_injection(self, user_input):
        # ?? Vuln�rabilit� : injection de commande shell
        return os.system(f"ping -c 1 {user_input}")
