from odoo import models, fields

class Customers(models.Model):
    _name = 'vc.customers'

    phone = fields.Char(string="phone", required=True)
    name = fields.Char(string="name", max_length=80, required=True)
