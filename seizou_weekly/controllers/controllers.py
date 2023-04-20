# -*- coding: utf-8 -*-
# from odoo import http


# class SeizouWeekly(http.Controller):
#     @http.route('/seizou_weekly/seizou_weekly/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/seizou_weekly/seizou_weekly/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('seizou_weekly.listing', {
#             'root': '/seizou_weekly/seizou_weekly',
#             'objects': http.request.env['seizou_weekly.seizou_weekly'].search([]),
#         })

#     @http.route('/seizou_weekly/seizou_weekly/objects/<model("seizou_weekly.seizou_weekly"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('seizou_weekly.object', {
#             'object': obj
#         })
