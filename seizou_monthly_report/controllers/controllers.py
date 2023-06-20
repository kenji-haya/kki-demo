# -*- coding: utf-8 -*-
# from odoo import http


# class SeizouMonthlyReport(http.Controller):
#     @http.route('/seizou_monthly_report/seizou_monthly_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/seizou_monthly_report/seizou_monthly_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('seizou_monthly_report.listing', {
#             'root': '/seizou_monthly_report/seizou_monthly_report',
#             'objects': http.request.env['seizou_monthly_report.seizou_monthly_report'].search([]),
#         })

#     @http.route('/seizou_monthly_report/seizou_monthly_report/objects/<model("seizou_monthly_report.seizou_monthly_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('seizou_monthly_report.object', {
#             'object': obj
#         })
