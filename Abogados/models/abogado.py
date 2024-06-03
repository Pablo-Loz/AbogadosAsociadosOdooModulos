from odoo import models, fields, api
from odoo.exceptions import ValidationError
from ..utils.dni_validation import validate_dni


class Abogado(models.Model):
    _name = 'abogados.abogado'
    _description = 'Abogado'
    _rec_name = 'nombre'

    # Campos Importantes
    nombre = fields.Char(string='Nombre', required=True)
    dni = fields.Char(string='DNI', size=9, help='Documento Nacional de Identidad')

    # Campos de Dirección
    direccion = fields.Char(string='Dirección')
    direccion_2 = fields.Char(string='Dirección 2')
    localidad = fields.Char(string='Localidad')
    codigo_postal = fields.Char(string='Código Postal')
    provincia = fields.Selection([
        ('Córdoba', 'Córdoba'),
        ('Granada', 'Granada'),
        ('Huelva', 'Huelva'),
        ('Jaén', 'Jaén'),
        ('Málaga', 'Málaga'),
        ('Sevilla', 'Sevilla'),
        ('Huesca', 'Huesca'),
        ('Teruel', 'Teruel'),
        ('Zaragoza', 'Zaragoza'),
        ('Asturias', 'Asturias'),
        ('Cantabria', 'Cantabria'),
        ('Albacete', 'Albacete'),
        ('Ciudad Real', 'Ciudad Real'),
        ('Cuenca', 'Cuenca'),
        ('Guadalajara', 'Guadalajara'),
        ('Toledo', 'Toledo'),
        ('Avila', 'Avila'),
        ('Burgos', 'Burgos'),
        ('León', 'León'),
        ('Palencia', 'Palencia'),
        ('Almería', 'Almería'),
        ('Cádiz', 'Cádiz'),
        ('Salamanca', 'Salamanca'),
        ('Segovia', 'Segovia'),
        ('Soria', 'Soria'),
        ('Valladolid', 'Valladolid'),
        ('Zamora', 'Zamora'),
        ('Barcelona', 'Barcelona'),
        ('Girona', 'Girona'),
        ('Lleida', 'Lleida'),
        ('Tarragona', 'Tarragona'),
        ('Badajoz', 'Badajoz'),
        ('Cáceres', 'Cáceres'),
        ('A Coruña', 'A Coruña'),
        ('Lugo', 'Lugo'),
        ('Ourense', 'Ourense'),
        ('Pontevedra', 'Pontevedra'),
        ('Las Palmas', 'Las Palmas'),
        ('S.C.Tenerife', 'S.C.Tenerife'),
        ('La Rioja', 'La Rioja'),
        ('Madrid', 'Madrid'),
        ('Murcia', 'Murcia'),
        ('Navarra', 'Navarra'),
        ('Alava', 'Alava'),
        ('Guipuzcoa', 'Guipuzcoa'),
        ('Vizcaya', 'Vizcaya'),
        ('Alicante', 'Alicante'),
        ('Castellon', 'Castellon'),
        ('Valencia', 'Valencia'),
        ('Ceuta', 'Ceuta'),
        ('Melilla', 'Melilla'),
        ('Islas Baleares', 'Islas Baleares')
    ], default="Murcia")

    # Campos de Contacto
    telefono_fijo = fields.Char(string='Teléfono Fijo')
    telefono_movil = fields.Char(string='Teléfono Móvil')
    telefono_2 = fields.Char(string='Teléfono 2')
    email = fields.Char(string='Email')

    # Campos de Facturación
    banco = fields.Char(string='Banco')
    banco_cuenta = fields.Char(string='Cuenta Bancaria')

    # Campos Profesionales
    despacho = fields.Char(string='Despacho')
    colegio = fields.Char(string='Colegio')
    numero_colegiado = fields.Char(string='Número Colegial')
    tipo = fields.Selection([
        ('bufete', 'Abogado de Nuestro Bufete'),
        ('contrario', 'Abogado Contrario')
    ], string='Tipo de Abogado', required=True, default='bufete')

    # Campos de Observación
    observaciones = fields.Text(string='Observaciones')

    # Funciones que llaman a la validación
    @api.constrains('dni')
    def _check_dni(self):
        for record in self:
            validate_dni(record.dni)

    @api.onchange('dni')
    def _onchange_dni(self):
        if self.dni:
            try:
                 validate_dni(self.dni)
            except ValidationError as e:
                return {
                    'warning': {
                        'title': "Error de validación",
                        'message': str(e),
                    }
                }

    @api.model
    def create(self, vals):
        if 'dni' in vals:
            validate_dni(vals['dni'])
        return super(Abogado, self).create(vals)

    def write(self, vals):
        if 'dni' in vals:
            validate_dni(vals['dni'])
        return super(Abogado, self).write(vals)
