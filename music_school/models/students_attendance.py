from odoo import fields, models


class StudentsAttendance(models.Model):
    _name = "students.attendance"
    _description = 'Students Attendance'
    _rec_name = 'student_id'

    student_id = fields.Many2one('res.partner', string='Students',
                                 domain=[('student', '=', True)],
                                 help="Name of the student.")
    attendance = fields.Selection([('present', 'Present'),
                                   ('absent', 'Absent')], string='Attendance',
                                  help="Attendance selection field.")
    date = fields.Date(string='Date', help='Date of the student attendance.')
