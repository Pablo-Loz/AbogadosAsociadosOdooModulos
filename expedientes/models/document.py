from datetime import date, datetime

from odoo import models, fields, api


class Document(models.Model):
    _name = 'documents.document'
    _description = 'Document'

    def download_file(self):
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        url = f"{base_url}/web/content?model={self._name}&id={self.id}&filename_field=namedocument&field=archivo&download=true"
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'self',
        }

    name = fields.Char(string='Referencia del Documento')
    cliente = fields.Many2one('clientes.cliente', string='Cliente')
    expediente = fields.Many2one('expedientes.expediente', string='Expediente', ondelete='set null')
    observaciones = fields.Text(string='Observaciones')
    name_document = fields.Char(string='Nombre del Documento')
    fecha_subida = fields.Datetime(string='Fecha de Subida')
    fecha_asignacion_cliente = fields.Datetime(string='Fecha de Asignación al Cliente')
    fecha_asignacion_expediente = fields.Datetime(string='Fecha de Asignación del Expediente')
    archivo = fields.Binary(string='Archivo')

    @api.onchange('expediente')
    def _onchange_expediente(self):
        if self.expediente:
            self.fecha_asignacion_expediente = date.today()

    @api.onchange('archivo')
    def _onchange_archivo(self):
        if self.archivo:
            self.fecha_subida = date.today()

    @api.onchange('cliente')
    def _onchange_cliente(self):
        if self.cliente:
            self.fecha_asignacion_cliente = date.today()