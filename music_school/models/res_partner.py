from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    student = fields.Boolean(string='Is Student',
                             help='Used to mark the contact as a student.')
    classes = fields.Many2one('class.type', string='Joined Class',
                              help='Relation field use to connect the class '
                                   'type to the contact.')
    attendance_count = fields.Integer(String='Attendance Count',
                                      compute='_compute_attendance_count',
                                      help='Attendance count displaying field.')
    student_type = fields.Selection(
        [('part_time', 'Part Time'), ('full_time', 'Full Time')],
        string='Course Mode',
        help='Field used to define the student selected class type.')

    def class_attendance_view(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'class',
            'view_mode': 'tree',
            'res_model': 'students.attendance',
            'domain': [
                ('student_id', '=', self.id)],
            'context': "{'create': False}"}

    def _compute_attendance_count(self):
        for record in self:
            record.attendance_count = self.env[
                'students.attendance'].search_count(
                [('student_id', '=', record.id),
                 ('attendance', '=', 'present')])
