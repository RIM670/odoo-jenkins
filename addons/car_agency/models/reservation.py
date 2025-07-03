from email.policy import default

from odoo import fields,models, api
import json

class Reservation(models.Model):
    _name='car_reservation'

    customer_id=fields.Many2one("res.partner",strting="Customer Name",domain=[('is_company', '=', False)],required="1")

    cin_number=fields.Char(string="Cin Number", related="customer_id.cin_number")
    phone=fields.Char(string="Phone", related="customer_id.phone")
    email=fields.Char(string="Email", related="customer_id.email")

    agency_id=fields.Many2one("res.partner",string="Agency Name",domain=[('is_company', '=', True)],required="1")
    responsible_id=fields.Many2one('hr.employee', string="Responsible",related="agency_id.responsible_id")
    n_car_list_ids = fields.Many2many("agency.car",string="Car List",
                                    readonly=False)
    status = fields.Selection([('available', 'Available'), ('rented', 'Rented'),('damaged','Damaged')], string='State', default='available')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    company_id = fields.Many2one('res.company', store=True, copy=False,
                                 string="Company",
                                 default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id',
                                  default=lambda
                                      self: self.env.user.company_id.currency_id.id)
    price = fields.Monetary(string="Price Fee")
    dy_domain = fields.Char(string="dy_domain",compute = '_compute_dynamic_domain')

    is_rented = fields.Boolean(default=False)







    @api.depends('agency_id')
    def _compute_dynamic_domain(self):
        records = self.env['agency.car'].search([('agency_id', '=', self.agency_id.id),('status', '=', 'available')])
        self.dy_domain = json.dumps([('id', 'in', [])])
        if records:
            self.dy_domain =  json.dumps([('id', 'in', records.ids)])


    def action_rent(self):
        for rec in self.n_car_list_ids:
            rec.sudo().write({'status':'rented','start_date':self.start_date,'end_date':self.end_date})
        self.is_rented = True
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Cars Have Been Successfully Rented',
                'type': 'rainbow_man',
            }
        }


