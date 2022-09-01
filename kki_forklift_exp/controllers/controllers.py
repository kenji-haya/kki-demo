# -*- coding: utf-8 -*-
# from odoo import http


# class KkiForkliftExp(http.Controller):
#     @http.route('/kki_forklift_exp/kki_forklift_exp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_forklift_exp/kki_forklift_exp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_forklift_exp.listing', {
#             'root': '/kki_forklift_exp/kki_forklift_exp',
#             'objects': http.request.env['kki_forklift_exp.kki_forklift_exp'].search([]),
#         })

#     @http.route('/kki_forklift_exp/kki_forklift_exp/objects/<model("kki_forklift_exp.kki_forklift_exp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_forklift_exp.object', {
#             'object': obj
#         })
