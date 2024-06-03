from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.modulos.Abogados.utils.dni_validation import validate_dni


#from odoo.modulos.Abogados.utils.dni_validation import validate_dni

class Cliente(models.Model):
    _name = 'clientes.cliente'
    _description = 'Cliente'
    # Si no coge los campos para la búsqueda le obligamos a cogerlo
    _rec_name = 'nombre_completo'

    nombre_completo = fields.Char(string='Nombre del Cliente', required=True)
    dni = fields.Char(string='DNI')

    # Campos de Contacto
    telefono = fields.Char(string='Teléfono')
    telefono2 = fields.Char(string='Teléfono 2')
    email = fields.Char(string='Email')

    # Campos de dirección
    direccion = fields.Char(string='Dirección')
    direccion2 = fields.Char(string='Dirección 2')
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

    observaciones = fields.Text(string='Observaciones')

    tipo = fields.Selection([
        ('bufete', 'Cliente de Nuestro Bufete'),
        ('contrario', 'Cliente Contrario')
    ], string='Tipo de Cliente', required=True, default='bufete')

    # FUNCIONES QUE LLAMAN A LA VALIDACIÓN
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
        return super(Cliente, self).create(vals)

    def write(self, vals):
        if 'dni' in vals:
            validate_dni(vals['dni'])
        return super(Cliente, self).write(vals)


"""
Función para conseguir los nombres si nos sale la referencia de los modelos
EJ ->  clientes.cliente,265 
 def name_get(self):
     result = []
     for record in self:
         name = record.nombre_completo
         result.append((record.id, name))
     return result
"""
