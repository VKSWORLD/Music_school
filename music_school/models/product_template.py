from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    music_instrument = fields.Boolean(string='Music Instrument',
                                      help='Enable the boolean consider'
                                           ' as instrument.')
    event_ticket = fields.Boolean(string='Event Ticket',
                                  help='Used to mark the contact as a student.')
