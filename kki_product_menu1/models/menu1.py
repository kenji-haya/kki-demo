# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_product_menu1(models.Model):
    _name = 'kki_product_menu1.menu1'
    _description = 'kki_product_menu1.menu1'

    name = fields.Char("name")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
