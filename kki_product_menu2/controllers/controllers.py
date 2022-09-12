# -*- coding: utf-8 -*-
# from odoo import http


# class KkiProductMenu2(http.Controller):
#     @http.route('/kki_product_menu2/kki_product_menu2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_product_menu2/kki_product_menu2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_product_menu2.listing', {
#             'root': '/kki_product_menu2/kki_product_menu2',
#             'objects': http.request.env['kki_product_menu2.kki_product_menu2'].search([]),
#         })

#     @http.route('/kki_product_menu2/kki_product_menu2/objects/<model("kki_product_menu2.kki_product_menu2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_product_menu2.object', {
#             'object': obj
#         })
