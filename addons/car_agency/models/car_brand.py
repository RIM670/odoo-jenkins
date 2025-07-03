from odoo import fields,models

class Car_Brand(models.Model):
    _name='car.brand'

    name=fields.Char(string='Name')
    image=fields.Image(string='Image')
    description=fields.Text()
    agency=fields.Char(string='Agency')

    cars_ids= fields.One2many("agency.car","car_brand_id")

    number_cars = fields.Char(compute="_count_cars")


    def _count_cars(self):
        for rec in self:
             rec.number_cars = str(len(rec.cars_ids)) + ' Cars' if rec.cars_ids else 0