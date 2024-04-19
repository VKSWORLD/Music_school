from odoo import fields, models


class ServiceType(models.Model):
    _name = 'service.type'
    _description = 'Service Type'

    name = fields.Char(string='Name', help='Name of the service.')
    instrument = fields.Char(string='Instrument', help='Instrument used in the '
                                                       'service.')
    teacher_id = fields.Many2one('hr.employee', string='Teacher',
                                 domain=[('teacher', '=', True)],
                                 help='Teacher assigned to the lesson.')
