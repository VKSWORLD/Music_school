from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    teacher = fields.Boolean(string='Is Teacher', help='Used to mark the '
                                                       'employee as a teacher.')
