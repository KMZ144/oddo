from odoo import models, fields

class CertificateTypes(models.Model):
    _name = 'vc.ctypes'
    
    name = fields.Char(string="Certificate Type", required=True)
    certificates_id = fields.One2many(comodel_name="vc.certificates", inverse_name="ctypes_name" , string='Certificates',ondelete='cascade')