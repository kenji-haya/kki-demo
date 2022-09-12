# -*- coding: utf-8 -*-
# from odoo import http


# class KkiProduct(http.Controller):
#     @http.route('/kki_product/kki_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_product/kki_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_product.listing', {
#             'root': '/kki_product/kki_product',
#             'objects': http.request.env['kki_product.kki_product'].search([]),
#         })

#     @http.route('/kki_product/kki_product/objects/<model("kki_product.kki_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_product.object', {
#             'object': obj
#         })
