from odoo import models, fields

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    expediente_id = fields.Many2one('expedientes.expediente', string='Expediente Asociado')
    observaciones = fields.Text(string='Observaciones')
