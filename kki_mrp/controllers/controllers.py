# -*- coding: utf-8 -*-
# from odoo import http


# class KkiMrp(http.Controller):
#     @http.route('/kki_mrp/kki_mrp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_mrp/kki_mrp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_mrp.listing', {
#             'root': '/kki_mrp/kki_mrp',
#             'objects': http.request.env['kki_mrp.kki_mrp'].search([]),
#         })

#     @http.route('/kki_mrp/kki_mrp/objects/<model("kki_mrp.kki_mrp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_mrp.object', {
#             'object': obj
#         })
