from odoo import models, fields

class Festivo(models.Model):
    _name = 'festivo.festivo'
    _description = 'Día Festivo'

    nombre = fields.Char('Nombre del Festivo', required=True)
    fecha = fields.Date('Fecha del Festivo', required=True)
    region = fields.Selection([
        ('murcia', 'Murcia'),
        ('alicante', 'Alicante'),
        # Aqui podemos añadir mas regiones si es necesario
    ], string='Región', required=True, help="Región para la cual aplica el festivo.")