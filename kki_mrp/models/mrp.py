# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_mrp(models.Model):
    _inherit = "mrp.production"
    # _name = 'kki_mrp.kki_mrp'
    # _description = 'kki_mrp.kki_mrp'
    order_date = fields.Datetime("納品日", required=True)

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
