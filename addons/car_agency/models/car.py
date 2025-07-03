from odoo import fields, models,api, _
from odoo.exceptions import ValidationError


class Car(models.Model):
    _name = 'agency.car'

    _rec_name = 'car_model'


    name = fields.Char(string='Name')
    registration_number=fields.Integer(string='Registration Number')
    car_model=fields.Char(string='Model')
    mileage=fields.Float(string='Mileage')
    status = fields.Selection([('available', 'Available'), ('rented', 'Rented'),('damaged','Damaged')], string='State', default='available')
    start_date=fields.Date(string='Start Date')
    end_date=fields.Date(string='End Date')
    note=fields.Text(string="Note")

    car_brand_id = fields.Many2one('car.brand')
    agency_id = fields.Many2many('res.partner')



    def alt_action(self):
        self.ensure_one()

        return {'name': _('Print'),
                'type': 'ir.actions.act_window',
                'res_model': 'damaged.why',
                'view_mode': 'form' ,
                'target': 'new',
                'context': {'default_damaged_car_id': self.id}
                }
    def action_available(self):
        for rec in self :
            rec.status= "available"


    @api.onchange("registration_number")
    def _onchange_registration_number(self):
        for rec in self:
            if rec.registration_number < 0:
                raise ValidationError('negative value! please add a valid number')




    _sql_constraints = [
        ('unique_registration_number','unique("registration_number")','this Registration Number is exist!')
    ]

    @api.constrains('registration_number')
    def _check_registration_number(self):
        for rec in self:
            if len(str(rec.registration_number)) != 8:
                raise ValidationError('invalid Registration Number! please add 8 number')

