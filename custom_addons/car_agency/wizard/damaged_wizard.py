from odoo import fields, models ,api


class DamagedWizard(models.TransientModel):
    _name='damaged.why'

    damaged_car_id=fields.Many2one('agency.car')
    damage_description=fields.Text(string="Description")

    def action_confirm(self):
        # print("inside confirm action")
        # print('DESCRIPTION', self.damage_description)
        car = self.env['agency.car'].browse(self.damaged_car_id.id) #self.damaged_car_id.id = 2
        if car :
            # print('car found !!!!')
            car.note = self.damage_description
            car.status = "damaged"
            # print("description : ",car.note)




