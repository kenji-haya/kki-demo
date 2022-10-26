# -*- coding: utf-8 -*-
# from odoo import http


# class KkiPurchase(http.Controller):
#     @http.route('/kki_purchase/kki_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_purchase/kki_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_purchase.listing', {
#             'root': '/kki_purchase/kki_purchase',
#             'objects': http.request.env['kki_purchase.kki_purchase'].search([]),
#         })

#     @http.route('/kki_purchase/kki_purchase/objects/<model("kki_purchase.kki_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_purchase.object', {
#             'object': obj
#         })
