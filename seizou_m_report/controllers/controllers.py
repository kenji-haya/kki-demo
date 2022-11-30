# -*- coding: utf-8 -*-
# from odoo import http


# class SeizouMReport(http.Controller):
#     @http.route('/seizou_m_report/seizou_m_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/seizou_m_report/seizou_m_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('seizou_m_report.listing', {
#             'root': '/seizou_m_report/seizou_m_report',
#             'objects': http.request.env['seizou_m_report.seizou_m_report'].search([]),
#         })

#     @http.route('/seizou_m_report/seizou_m_report/objects/<model("seizou_m_report.seizou_m_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('seizou_m_report.object', {
#             'object': obj
#         })
