from odoo import  fields, models,api
from odoo.exceptions import ValidationError


class Customer (models.Model):
    _inherit = 'res.partner'

    name= fields.Char(string="Name")
    cin_number=fields.Char(string="Cin Number")
    phone=fields.Char(string="Phone")
    email=fields.Char(string="Email")





    _sql_constraints = [
        ('unique_cin_number','unique("cin_number")','this Cin number is exist!')
    ]

    @api.constrains('cin_number')
    def _check_cin_number(self):
        for rec in self:
            if not rec.is_company and len(rec.cin_number) != 8:
                raise ValidationError('invalid Cin Number! please add 8 number')
