# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_product_brand(models.Model):
    _name = 'kki_product_brand.brand'
    _description = 'kki_product_brand.brand'

    name = fields.Char("name")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
