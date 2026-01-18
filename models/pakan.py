from odoo import models, fields

class PakanBurung(models.Model):
    _name = 'pakan.burung'
    _description = 'Pakan Burung'

    name = fields.Char(required=True)
    jenis = fields.Selection([
        ('biji', 'Biji'),
        ('pelet', 'Pelet'),
        ('serbuk', 'Serbuk')
    ], required=True)

    harga = fields.Integer(required=True)
    stok = fields.Integer(default=0)
