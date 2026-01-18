from odoo import models, fields, api

class TransaksiPakan(models.Model):
    _name = 'pakan.transaksi'
    _description = 'Transaksi Penjualan Pakan'
    _rec_name = 'kode_transaksi'

    kode_transaksi = fields.Char(
        default=lambda self: self.env['ir.sequence'].next_by_code('pakan.transaksi'),
        readonly=True
    )

    tanggal = fields.Date(default=fields.Date.today)
    customer_id = fields.Many2one('pakan.partner', domain=[('tipe', '=', 'customer')])
    pakan_id = fields.Many2one('pakan.burung')
    qty = fields.Integer(default=1)
    harga_satuan = fields.Integer(related='pakan_id.harga')
    total = fields.Integer(compute='_compute_total', store=True)

    @api.depends('qty', 'harga_satuan')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.qty * rec.harga_satuan

    def action_confirm(self):
        for rec in self:
            rec.pakan_id.stok -= rec.qty
