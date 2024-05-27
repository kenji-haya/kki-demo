# -*- coding: utf-8 -*-
# from odoo import http


# class KkiForklift(http.Controller):
#     @http.route('/kki_forklift/kki_forklift/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_forklift/kki_forklift/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_forklift.listing', {
#             'root': '/kki_forklift/kki_forklift',
#             'objects': http.request.env['kki_forklift.kki_forklift'].search([]),
#         })

#     @http.route('/kki_forklift/kki_forklift/objects/<model("kki_forklift.kki_forklift"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_forklift.object', {
#             'object': obj
#         })
