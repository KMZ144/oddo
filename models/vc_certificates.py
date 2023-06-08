from odoo import models, fields, api


class CertificatesApp(models.Model):
    _name = 'vc.certificates'

    # Define Automatic Serial Number    
    serial_number = fields.Char(string="Serial Number", default=lambda self: self._default_cert_number_seq())
    _sql_constraints = [('serial_number_unique', 'unique(serial_number)', 'The Serial Number must be unique!')]

    vehicle_type = fields.Selection(
        [('Car', 'Car'), ('Bus', 'Bus'), ('Mini bus', 'Mini bus'), ('Micro bus', 'Micro bus')], string="Vehicle Type",
        required=True)
    ctypes_name = fields.Many2one(comodel_name='vc.ctypes', string="Certificate Type", ondelete='cascade')
    dept_name = fields.Many2one(comodel_name='vc.dept', string="Traffic Department", ondelete='cascade')
    customer_name = fields.Many2one(comodel_name='res.partner', string="Customer", ondelete='cascade')

    price = fields.Float(string="Price", required=True)
    motor_number = fields.Char(string="Motor Number", required=True)
    chassis_number = fields.Char(string="Chassis Number", required=True)
    car_model = fields.Selection('_get_year_list', string="Car Model", required=True)
    brand = fields.Many2one(comodel_name='vc.brand', string="Brand", required=True, ondelete='cascade')

    allow_printing = fields.Boolean(default=True)
    print_logs_ids = fields.One2many("certificates.logs", "certificate_id")

    @api.depends('serial_number')
    def _default_cert_number_seq(self):
        serial_number_sequence = self.env['ir.sequence'].create({
            'name': 'Serial Number Sequence',
            'code': 'serial_number_sequence',
            'prefix': 'TD',
            'padding': 5
        })
        serial_number = serial_number_sequence.next_by_id()
        return serial_number

    @api.model
    def _get_year_list(self):
        current_year = fields.Date.today().year
        years = range(current_year - 20, current_year + 1)
        return [(str(year), str(year)) for year in years]

    def print_report(self):
        self.certificate_print_log()
        return self.env.ref("vc.certificates_report").report_action(self)

    def certificate_print_log(self):
        self.env["certificates.logs"].create({
            "certificate_id": self.id
        })

    def allow_reprint_report(self):
        self.allow_printing = True


class LogHistory(models.Model):
    _name = "certificates.logs"
    certificate_id = fields.Many2one("vc.certificates")