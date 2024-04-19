from datetime import timedelta
from odoo import api, fields, models


class ClassType(models.Model):
    _name = 'class.type'
    _description = 'Class Type'

    name = fields.Char(string='Name', help='Class name.')
    from_date = fields.Date(string='From', help='Class starting date.')
    to_date = fields.Date(string='To', help='Class ending date.')
    duration = fields.Integer(string='Duration', compute='_compute_duration',
                              store=True, help='Duration of the class.')
    service_id = fields.Many2one('service.type', string='Services',
                                 help='Type of service.')
    instrument_id = fields.Many2one('product.product',
                                    String='Instrument',
                                    domain=[('music_instrument', '=', True)],
                                    help='Instrument used in the music class.')
    teacher_id = fields.Many2one('hr.employee', string='Teacher',
                                 domain=[('teacher', '=', True)],
                                 help='Teacher name.')
    location = fields.Char(string='Location', help='Location of the class.')
    repeats = fields.Selection(selection=[('weekly', 'Weekly'),
                                          ('monthly', 'Monthly')],
                               string='Repeats',
                               help='Repeated days per week.')
    state = fields.Selection(
        selection=[('draft', 'Draft'), ('started', 'Started'),
                   ('completed', 'Completed'),
                   ('invoice', 'Invoiced'), ('canceled', 'Canceled')],
        default='draft', help='State of the class.')
    lesson_ids = fields.One2many('class.lesson',
                                 'relation_id',
                                 String='Class Lessons',
                                 help='Daily class lessons records.')
    student_ids = fields.Many2many('res.partner', string='Student',
                                   domain=[('student', '=', True)],
                                   String='Student ID',
                                   help='Student who joined in the class.')
    order_count = fields.Integer(compute='_compute_order_count',
                                 String='Order Count',
                                 help='Total count of the invoice.')
    sunday = fields.Boolean(string='Sunday', help='Mark the day as a workday.')
    monday = fields.Boolean(string='Monday', help='Mark the day as a workday.')
    tuesday = fields.Boolean(string='Tuesday',
                             help='Mark the day as a workday.')
    wednesday = fields.Boolean(string='Wednesday',
                               help='Mark the day as a workday.')
    thursday = fields.Boolean(string='Thursday',
                              help='Mark the day as a workday.')
    friday = fields.Boolean(string='Friday', help='Mark the day as a workday.')
    saturday = fields.Boolean(string='Saturday',
                              help='Mark the day as a workday.')

    @api.depends('from_date', 'to_date')
    def _compute_duration(self):
        for records in self:
            if records.from_date and records.to_date:
                num_work_days = 0
                current_date = records.from_date
                while current_date <= records.to_date:
                    if current_date.weekday() < 5:
                        num_work_days += 1
                    current_date += timedelta(days=1)
                self.duration = num_work_days

    def action_button_class_start(self):
        self.write({'state': 'started'})
        return self._compute_duration()

    def action_button_set_to_draft(self):
        self.write({'state': 'draft'})

    def action_button_class_cancel(self):
        self.write({'state': 'canceled'})

    def action_button_class_completed(self):
        self.write({'state': 'completed'})

    def action_button_create_order(self):
        for student in self.student_ids:
            self.env['account.move'].create([
                {'move_type': 'out_invoice',
                 'partner_id': student.id,
                 'invoice_date': self.from_date,
                 'invoice_line_ids': [(0, 0, {
                     'product_id': self.instrument_id.id,
                     'price_unit': self.instrument_id.lst_price,
                     'quantity': self.duration})]}])
        self.write({'state': 'invoice'})

    def related_order(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'view_mode': 'tree',
            'res_model': 'account.move',
            'domain': [('partner_id', 'in', self.student_ids.ids)],
            'context': {'create': False}}

    def _compute_order_count(self):
        for record in self:
            record.order_count = self.env['account.move'].search_count(
                [('partner_id', 'in', self.student_ids.ids)])
