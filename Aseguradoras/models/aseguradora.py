from odoo import models, fields

class Aseguradora(models.Model):
    _name = 'aseguradoras.aseguradora'
    _description = 'Aseguradoras'
    _rec_name = 'nombre_completo'

    dni = fields.Char(string='DNI', size=9, help='DNI')
    nombre_completo = fields.Char(string='Nombre Aseguradora', required=True)
    telefono = fields.Char(string='Teléfono')
    telefono_2 = fields.Char(string='Teléfono 2')
    direccion = fields.Char(string='Dirección')
    direccion_2 = fields.Char(string='Dirección 2')
    email = fields.Char(string='Email')
    localidad = fields.Char(string='Localidad')
    poblacion = fields.Char(string='Población')
    provincia = fields.Selection([
        ('cordoba', 'Córdoba'),
        ('granada', 'Granada'),
        ('huelva', 'Huelva'),
        ('jaen', 'Jaén'),
        ('malaga', 'Málaga'),
        ('sevilla', 'Sevilla'),
        ('huesca', 'Huesca'),
        ('teruel', 'Teruel'),
        ('zaragoza', 'Zaragoza'),
        ('asturias', 'Asturias'),
        ('cantabria', 'Cantabria'),
        ('albacete', 'Albacete'),
        ('ciudad_real', 'Ciudad Real'),
        ('cuenca', 'Cuenca'),
        ('guadalajara', 'Guadalajara'),
        ('toledo', 'Toledo'),
        ('avila', 'Avila'),
        ('burgos', 'Burgos'),
        ('leon', 'León'),
        ('palencia', 'Palencia'),
        ('almeria', 'Almería'),
        ('cadiz', 'Cádiz'),
        ('salamanca', 'Salamanca'),
        ('segovia', 'Segovia'),
        ('soria', 'Soria'),
        ('valladolid', 'Valladolid'),
        ('zamora', 'Zamora'),
        ('barcelona', 'Barcelona'),
        ('girona', 'Girona'),
        ('lleida', 'Lleida'),
        ('tarragona', 'Tarragona'),
        ('badajoz', 'Badajoz'),
        ('caceres', 'Cáceres'),
        ('a_coruna', 'A Coruña'),
        ('lugo', 'Lugo'),
        ('ourense', 'Ourense'),
        ('pontevedra', 'Pontevedra'),
        ('las_palmas', 'Las Palmas'),
        ('s_c_tenerife', 'S.C.Tenerife'),
        ('la_rioja', 'La Rioja'),
        ('madrid', 'Madrid'),
        ('murcia', 'Murcia'),
        ('navarra', 'Navarra'),
        ('alava', 'Alava'),
        ('guipuzcoa', 'Guipuzcoa'),
        ('vizcaya', 'Vizcaya'),
        ('alicante', 'Alicante'),
        ('castellon', 'Castellon'),
        ('valencia', 'Valencia'),
        ('ceuta', 'Ceuta'),
        ('melilla', 'Melilla'),
        ('islas_baleares', 'Islas Baleares')
    ], default="murcia")
    codigo_postal = fields.Char(string='Código Postal', size=5)
    web = fields.Char(string='Página Web', help='Dirección de la página web')
    poblacion_2 = fields.Char(string='Población')
    provincia_2 = fields.Char(string='Provincia')
    codigo_postal_2 = fields.Char(string='Código Postal', size=5)
    web_2 = fields.Char(string='Página Web', help='Dirección de la página web')

    banco = fields.Char(string='Banco')
    numero_de_cuenta = fields.Char(string='Número de cuenta')
