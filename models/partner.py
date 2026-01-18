from odoo import models, fields

class PartnerPakan(models.Model):
    _name = 'pakan.partner'
    _description = 'Pelanggan & Supplier'

    name = fields.Char(required=True)
    tipe = fields.Selection([
        ('customer', 'Pelanggan'),
        ('supplier', 'Supplier')
    ], required=True)

    phone = fields.Char()
    email = fields.Char()
    alamat = fields.Text()
