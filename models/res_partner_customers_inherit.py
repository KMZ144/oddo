from odoo import models, fields

class CustomersInherit(models.Model):
    _inherit = 'res.partner'

    related_certificate_id = fields.Many2one("vc.certificates", string="Customer")
                