from odoo import models, fields

class CRMPakan(models.Model):
    _name = 'pakan.crm'
    _description = 'CRM Pakan Burung'

    name = fields.Char(string='Nama Lead', required=True)
    customer_id = fields.Many2one('pakan.partner')
    status = fields.Selection([
        ('new', 'New'),
        ('followup', 'Follow Up'),
        ('deal', 'Deal'),
        ('lost', 'Lost')
    ], default='new')

    catatan = fields.Text()
