# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class penjualan_pakan_burung(models.Model):
#     _name = 'penjualan_pakan_burung.penjualan_pakan_burung'
#     _description = 'penjualan_pakan_burung.penjualan_pakan_burung'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

