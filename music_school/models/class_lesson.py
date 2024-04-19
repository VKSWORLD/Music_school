from odoo import fields, models


class ClassLesson(models.Model):
    _name = 'class.lesson'
    _description = 'Class Lesson'

    name = fields.Char(string='Name', help='Name of the lesson.')
    hours = fields.Char(string='Hours', help='Hours of the lesson.')
    teacher_id = fields.Many2one('hr.employee', string='Teacher',
                                 domain=[('teacher', '=', True)],
                                 help='Teacher assigned to the lesson.')
    relation_id = fields.Many2one('class.type',
                                  string='Relation ID',
                                  help='Relation to the corresponding class.')
