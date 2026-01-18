# -*- coding: utf-8 -*-
# from odoo import http


# class PenjualanPakanBurung(http.Controller):
#     @http.route('/penjualan_pakan_burung/penjualan_pakan_burung', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/penjualan_pakan_burung/penjualan_pakan_burung/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('penjualan_pakan_burung.listing', {
#             'root': '/penjualan_pakan_burung/penjualan_pakan_burung',
#             'objects': http.request.env['penjualan_pakan_burung.penjualan_pakan_burung'].search([]),
#         })

#     @http.route('/penjualan_pakan_burung/penjualan_pakan_burung/objects/<model("penjualan_pakan_burung.penjualan_pakan_burung"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('penjualan_pakan_burung.object', {
#             'object': obj
#         })

