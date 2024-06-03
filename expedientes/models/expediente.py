from odoo import models, fields, api
import datetime
class Expediente(models.Model):
    _name = 'expedientes.expediente'
    _description = 'Expediente'

    # Hacer el campo name editable para la importación
    name = fields.Char(string='Número de referencia del expediente', required=True, readonly=True,
                       default=lambda self: self._default_name())

    # Función para generar el nombre del expediente automáticamente
    def _default_name(self):
        # Se obtiene el próximo número disponible de la secuencia
        sequence = self.env['ir.sequence'].next_by_code('expedientes.expediente')
        anyoa_ctual = datetime.datetime.now().year  # Obtener el año actual
        # Formatear el nombre del expediente como 'EXP-<Número>-<Año>'
        return "EXP-{}/{}".format(sequence, current_year)

    tramites_ids = fields.One2many('tramites.tramite', 'expediente_id', string='Trámites Asociados')
    documentos_ids = fields.One2many('documents.document', 'expediente', string='Documentos Asociados')

    cliente = fields.Many2one(
        'clientes.cliente',
        string='Clientes',
        domain=[('tipo', '=', 'bufete')],
        help="Seleccione un cliente que sea parte del bufete."
    )
    cliente_contrario = fields.Many2one(
        'clientes.cliente',
        string='Clientes Contrarios',
        domain=[('tipo', '=', 'contrario')],
        help="Seleccione un cliente que sea parte de los contrarios."
    )

    abogados = fields.Many2one(
        'abogados.abogado',
        string='Abogados',
        domain=[('tipo', '=', 'bufete')],
        help="Seleccione un abogado que sea parte del bufete."
    )
    abogados_contrarios = fields.Many2one(
        'abogados.abogado',
        string='Abogados Contrarios',
        domain=[('tipo', '=', 'contrario')],  # Solo abogados contrarios
        help="Seleccione un abogado que sea parte de los contrarios."
    )

    juzgado = fields.Many2one(
        'juzgados.juzgado', string='Juzgado'
    )
    aseguradora = fields.Many2one(
        'aseguradoras.aseguradora', string='Aseguradora'
    )
    aseguradora_contraria = fields.Many2one(
        'aseguradoras.aseguradora', string='Aseguradora Contraria'
    )
    perito = fields.Many2one(
        'peritos.perito', string='Perito'
    )
    perito_contrarios = fields.Many2one(
        'peritos.perito',
        string='Perito Contrario',
        domain=[('tipo', '=', 'contrario')],
        help="Seleccione un perito que sea parte de los contrarios."
    )

    procurador = fields.Many2one(
        'procuradores.procurador', string='Procurador'
    )
    procurador_contrarios = fields.Many2one(
        'procuradores.procurador',
        string='Procurador Contrario',
        domain=[('tipo', '=', 'contrario')],
        help="Seleccione un procurador que sea parte de los contrarios."
    )

    descripcion = fields.Text(string='Descripción')
    alta_expediente = fields.Datetime(string='Fecha de alta del expediente', default=fields.Date.today)
    cierre_expediente = fields.Datetime(string='Fecha de cierre del expediente')
    turno_oficio = fields.Boolean(string='Turno de oficio', help="Marque este campo si el expediente está asignado al turno de oficio.")
    observacion = fields.Text(string="Observaciones")

    fecha_siniestro = fields.Date(string='Fecha de siniestro')
    fecha_denuncia = fields.Date(string='Fecha de denuncia')
    fecha_consignacion = fields.Date(string='Fecha de consignación')
    cuantia_materiales = fields.Float(string='Cuantía materiales')
    cuantia_personales = fields.Float(string='Cuantía personales')
    responsabilidad_civil_directa = fields.Char(string='Responsabilidad civil directa')

    jurisdiccion = fields.Selection([
        ('extrajudicial', 'EXTRAJUDICIAL'),
        ('jurisdiccion_civil_y_mercantil', 'JURISDICCIÓN CIVIL Y MERCANTIL'),
        ('jurisdiccion_penal', 'JURISDICCIÓN PENAL'),
        ('jurisdiccion_social', 'JURISDICCIÓN SOCIAL'),
        ('administrativo_y_fiscal', 'ADMINISTRATIVO y FISCAL'),
        ('contencioso_administrativo', 'CONTENCIOSO - ADMINISTRATIVO'),
        ('tribunal_constitucional', 'TRIBUNAL CONSTITUCIONAL'),
        ('derecho_comunitario', 'DERECHO COMUNITARIO'),
        ('aseguradoras', 'ASEGURADORAS'),
        ('jurisdiccion_ecclesiastica', 'JURISDICCIÓN ECLESIÁSTICA'),
        ('jurisdiccion_militar', 'JURISDICCIÓN MILITAR'),
        ('otros', 'OTROS'),
        ('jurisdiccion_civil_2', 'JURISDICCION CIVIL'),
        ('jurisdiccion_penal_2', 'JURISDICCION PENAL'),
        ('contencioso_administrativo_2', 'CONTENCIOSO-ADMINISTRATIVO'),
        ('jurisdiccion_social_2', 'JURISDICCION SOCIAL'),
        ('turno_de_oficio', 'TURNO DE OFICIO'),
        ('administrativo_2', 'ADMINISTRATIVO'),
        ('familia', 'FAMILIA'),
        ('estafa', 'ESTAFA'),
        ('contratos', 'CONTRATOS'),
        ('menores', 'MENORES'),
        ('tribunal_eclesiastico', 'TRIBUNAL ECLASIÁSTICO')
    ], string='Tipo de Jurisdicción')

    asunto_jurisdiccion = fields.Char(string="Asunto de la Jurisdiccion")

    total_costas = fields.Float(string='Total costas')
    prevision_de_fondos = fields.Float(string='Previsión de fondos')
    importe_suplidos = fields.Float(string='Importe de suplidos')
    importe_honorarios = fields.Float(string='Importe de honorarios')
    importe_anticipos = fields.Float(string='Importe de anticipos')
    importe_gastos = fields.Float(string='Importe de gastos')
    importe_descuentos = fields.Float(string='Importe de descuentos')
    importe_iva = fields.Float(string='Importe de IVA')
    importe_irpf = fields.Float(string='Importe de IRPF')
    importe_total = fields.Float(string='Importe total')
    importe_neto = fields.Float(string='Importe neto')

    cliente_colectivo = fields.Many2many(
        'clientes.cliente',
        'expediente_cliente_rel',  # Este es el nombre de la tabla de relación
        'expediente_id',  # Columna para este modelo
        'cliente_id',  # Columna para el modelo relacionado
        string='Clientes Colectivos',
        domain=[('tipo', '=', 'bufete')],
        help="Seleccione clientes que sean parte del bufete."
    )
    cliente_contrario_colectivo = fields.Many2many(
        'clientes.cliente',
        'expediente_clientecontrario_rel',
        'expediente_id',
        'cliente_id',
        string='Contrarios Colectivo',
        domain=[('tipo', '=', 'contrario')],
        help="Seleccione clientes que sean parte de los contrarios."
    )

    peritos = fields.Many2many(
        'peritos.perito',
        'expediente_perito_rel',
        'expediente_id',
        'perito_id',
        string='Peritos Colectivo',
        domain=[('tipo', '=', 'bufete')],
        help="Seleccione peritos que sean parte de los contrarios."
    )
    peritos2 = fields.Many2many(
        'peritos.perito',
        'expediente_perito2_rel',
        'expediente_id',
        'perito_id',
        string='Peritos Contrarios Colectivo',
        domain=[('tipo', '=', 'bufete')],
        help="Seleccione peritos que sean parte de los contrarios."
    )
    abogados_colectivo = fields.Many2many(
        'abogados.abogado',
        'expediente_abogado_rel',
        'expediente_id',
        'abogado_id',
        string='Abogados Colectivos',
        domain=[('tipo', '=', 'bufete')],
        help="Seleccione abogados que sean parte del bufete."
    )
    abogados_contrarios_colectivo = fields.Many2many(
        'abogados.abogado',
        'expediente_abogadocontrario_rel',
        'expediente_id',
        'abogado_id',
        string='Abogados Contrarios Colectivos',
        domain=[('tipo', '=', 'contrario')],
        help="Seleccione abogados que sean parte de los contrarios."
    )

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = ['|', ('name', operator, name), ('descripcion', operator, name)]
        records = self.search(domain + args, limit=limit)
        return records.name_get()

    def name_get(self):
        result = []
        for record in self:
            name = record.descripcion or record.name
            result.append((record.id, name))
        return result