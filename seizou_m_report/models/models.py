# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class seizou_m_report(models.Model):
#     _name = 'seizou_m_report.seizou_m_report'
#     _description = 'seizou_m_report.seizou_m_report'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
