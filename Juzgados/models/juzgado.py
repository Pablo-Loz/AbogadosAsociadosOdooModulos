from odoo import models, fields


class Juzgado(models.Model):
    _name = 'juzgados.juzgado'
    _description = 'Juzgados'
    _rec_name = 'nombre_completo'

    nombre_completo = fields.Char(string='Nombre del Juzgado', required=True)

    telefono = fields.Char(string='Teléfono')
    telefono_2 = fields.Char(string='Teléfono 2')
    direccion = fields.Char(string='Dirección')
    direccion_2 = fields.Char(string='Dirección 2')
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

    num_auto = fields.Char(string='Número de Auto')
    observaciones = fields.Text(string='Observaciones')

    banco = fields.Char(string='Banco')
    numero_de_cuenta = fields.Char(string='Número de cuenta')
