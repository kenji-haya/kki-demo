# -*- coding: utf-8 -*-
# from odoo import http


# class KkiInfo(http.Controller):
#     @http.route('/kki_info/kki_info/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_info/kki_info/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_info.listing', {
#             'root': '/kki_info/kki_info',
#             'objects': http.request.env['kki_info.kki_info'].search([]),
#         })

#     @http.route('/kki_info/kki_info/objects/<model("kki_info.kki_info"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_info.object', {
#             'object': obj
#         })
