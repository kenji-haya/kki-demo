# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_purchase(models.Model):
    # _name = 'kki_purchase.kki_purchase'
    # _description = 'kki_purchase.kki_purchase'
    _inherit = "purchase.order"

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
