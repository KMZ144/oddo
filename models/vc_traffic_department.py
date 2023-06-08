from odoo import models, fields

class TrafficDepartment(models.Model):
    _name = 'vc.dept'
    
    name = fields.Char(string="Traffic Department", required=True)
    certificates_id = fields.One2many(comodel_name="vc.certificates", inverse_name="dept_name", string='Certificates',ondelete='cascade')