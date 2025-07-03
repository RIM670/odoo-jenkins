from odoo import fields, models

class Agency(models.Model):
    _inherit = 'res.partner'

    responsible_id=fields.Many2one('hr.employee', string="Responsible")

    new_car_list_ids=fields.Many2many("agency.car")