from odoo import models, fields, api
from odoo.exceptions import ValidationError
from ..utils.dni_validation import validate_dni

class Procurador(models.Model):
    _name = 'procuradores.procurador'
    _description = 'Procuradores'
    _rec_name = 'nombre_completo'

    dni = fields.Char(string='DNI', size=9, help='Documento Nacional de Identidad')
    nombre_completo = fields.Char(string='Nombre Procurador', required=True)

    # Campos de dirección
    direccion = fields.Char(string='Dirección')
    direccion_2 = fields.Char(string='Dirección 2')
    localidad = fields.Char(string='Localidad')
    poblacion = fields.Char(string='Población')
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
    codigo_postal = fields.Char(string='Código Postal', size=5)
    poblacion_2 = fields.Char(string='Población 2')
    provincia_2 = fields.Char(string='Provincia 2')
    codigo_postal_2 = fields.Char(string='Código Postal 2', size=5)

    # Campos de Contacto
    email = fields.Char(string='Email')
    web = fields.Char(string='Página Web', help='Dirección de la página web')
    telefono = fields.Char(string='Teléfono')
    telefono_2 = fields.Char(string='Teléfono 2')
    web_2 = fields.Char(string='Página Web 2', help='Dirección de la página web')

    # Campos de Facturación
    banco = fields.Char(string='Banco')
    numero_de_cuenta = fields.Char(string='Número de cuenta')

    # Información Profesional
    colegios = fields.Char(string='Colegios')
    colegiado = fields.Char(string='Colegiado')
    despacho = fields.Char(string='Despacho')

    tipo = fields.Selection([
        ('bufete', 'Procurador de Nuestro Bufete'),
        ('contrario', 'Procurador Contrario')
    ], string='Tipo de Procurador', required=True, default='bufete')

     #Funciones que llaman a la validación
    #@api.constrains('dni')
    #def _check_dni(self):
     #   for record in self:
      #      validate_dni(record.dni)

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
        return super(Procurador, self).create(vals)

    def write(self, vals):
        if 'dni' in vals:
            validate_dni(vals['dni'])
        return super(Procurador, self).write(vals)
