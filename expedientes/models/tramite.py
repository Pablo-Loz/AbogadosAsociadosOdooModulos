from datetime import timedelta, datetime

from odoo import models, fields, api


class Tramite(models.Model):
    _name = 'tramites.tramite'
    _description = 'Clase que permitira crear instancias de los diferentes tramites'

    name = fields.Char(string='Nombre del Trámite', required=True)
    region = fields.Selection([
        ('murcia', 'Murcia'),
        ('alicante', 'Alicante'),
    ], string='Región', required=True, help="Seleccione la región para calcular los días festivos correspondientes.",
        default='murcia')

    expediente_id = fields.Many2one('expedientes.expediente', string='Expediente asociado', ondelete='set null')
    observaciones = fields.Text(string='Observaciones')
    crear_expediente = fields.Boolean(string='Crear Expediente', default=False)
    descripcion = fields.Text(string='Descripcion del Tramite')
    Fecha_Presentacion = fields.Date(string='Fecha de Presentación', default=fields.Date.today,
                                    help="Fecha de cuando se presentan los documentos")
    Fecha_Inicio = fields.Date(string='Fecha de Inicio',
                              help="La fecha de Inicio desde donde se quiere empezar a contar los dias")
    dias_habiles = fields.Integer(string='Días Hábiles')
    Fecha_Vencimiento = fields.Date(string='Fecha de Vencimiento', compute='_calcular_fecha_vencimiento')
    crear_en_calendario = fields.Boolean(string='Crear Evento en Calendario', default=False)

    @api.model
    def create(self, vals):
        # Primero creas el trámite
        tramite = super(Tramite, self).create(vals)

        # Comprueba si se debe crear un evento en el calendario
        if tramite.crear_en_calendario:
            self.env['calendar.event'].create({
                'name': tramite.name,
                'start': tramite.Fecha_Inicio,  
                'stop': tramite.Fecha_Vencimiento,
                'allday': True,
                'description': tramite.observaciones,
            })
        return tramite

    @api.depends('Fecha_Presentacion', 'dias_habiles', 'region')
    def _calcular_fecha_vencimiento(self):
        for record in self:
            if not (record.Fecha_Inicio and record.dias_habiles and record.region):
                record.Fecha_Vencimiento = False
                continue
            fecha_inicio = fields.Date.from_string(record.FechaInicio)
            fecha_final = fecha_inicio
            dias_agregados = 0
            while dias_agregados < record.dias_habiles:
                fecha_final += timedelta(days=1)
                if fecha_final.weekday() < 5:
                    festivos = self.env['festivo.festivo'].search([
                        ('fecha', '=', fecha_final),
                        ('region', '=', record.region)
                    ])
                    if not festivos:
                        dias_agregados += 1
            record.Fecha_Vencimiento = fecha_final

    def _default_expediente_name(self):
        # Se obtiene el próximo número disponible de la secuencia
        sequence = self.env['ir.sequence'].next_by_code('expedientes.expediente')
        current_year = datetime.now().year  # Obtener el año actual
        # Formatear el nombre del expediente como 'EXP-Número/Año'
        return "EXP-{}/{}".format(sequence, current_year)

    @api.model
    def create(self, vals):
        if vals.get('crear_expediente') and not vals.get('expediente_id'):
            expediente_name = self._default_expediente_name()
            expediente = self.env['expedientes.expediente'].create({'name': expediente_name})
            vals['expediente_id'] = expediente.id
        return super(Tramite, self).create(vals)

    @api.onchange('crear_expediente')
    def _onchange_crear_expediente(self):
        if self.crear_expediente and not self.expediente_id:
            expediente_name = self._default_expediente_name()
            expediente = self.env['expedientes.expediente'].create({'name': expediente_name})
            self.expediente_id = expediente.id




