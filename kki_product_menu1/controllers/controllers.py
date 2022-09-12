# -*- coding: utf-8 -*-
# from odoo import http


# class KkiProductMenu1(http.Controller):
#     @http.route('/kki_product_menu1/kki_product_menu1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_product_menu1/kki_product_menu1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_product_menu1.listing', {
#             'root': '/kki_product_menu1/kki_product_menu1',
#             'objects': http.request.env['kki_product_menu1.kki_product_menu1'].search([]),
#         })

#     @http.route('/kki_product_menu1/kki_product_menu1/objects/<model("kki_product_menu1.kki_product_menu1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_product_menu1.object', {
#             'object': obj
#         })
