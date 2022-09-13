# -*- coding: utf-8 -*-
# from odoo import http


# class KkiProductBrand(http.Controller):
#     @http.route('/kki_product_brand/kki_product_brand/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_product_brand/kki_product_brand/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_product_brand.listing', {
#             'root': '/kki_product_brand/kki_product_brand',
#             'objects': http.request.env['kki_product_brand.kki_product_brand'].search([]),
#         })

#     @http.route('/kki_product_brand/kki_product_brand/objects/<model("kki_product_brand.kki_product_brand"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_product_brand.object', {
#             'object': obj
#         })
