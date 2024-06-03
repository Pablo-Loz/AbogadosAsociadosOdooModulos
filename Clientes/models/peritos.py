from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.modulos.Abogados.utils.dni_validation import validate_dni

class Perito(models.Model):
    _name = 'peritos.perito'
    _description = 'Peritos'
    # Si no coge los campos para la busqueda le obligamos a cogerlo
    _rec_name = 'nombre_completo'

    nombre_completo = fields.Char(string='Nombre del Perito/Otro', required=True)
    dni = fields.Char(string='DNI')

    telefono = fields.Char(string='Teléfono')
    telefono2 = fields.Char(string='Teléfono 2')
    direccion = fields.Char(string='Dirección')
    direccion2 = fields.Char(string='Dirección 2')
    email = fields.Char(string='Email')
    localidad = fields.Char(string='Localidad')
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
    tipo = fields.Selection([
        ('bufete', 'Perito de Nuestro Bufete'),
        ('contrario', 'Perito Contrario')
    ], string='Tipo de Perito', required=True, default='bufete')

    observaciones = fields.Text(string='Observaciones')

    # FUNCIONES QUE LLAMAN A LA VALIDACION
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
        return super(Perito, self).create(vals)

    def write(self, vals):
        if 'dni' in vals:
            validate_dni(vals['dni'])
        return super(Perito, self).write(vals)
