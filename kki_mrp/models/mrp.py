# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_mrp(models.Model):
    _inherit = "mrp.production"
    # _name = 'kki_mrp.kki_mrp'
    # _description = 'kki_mrp.kki_mrp'
    # order_date = fields.Datetime("納品日", required=True)
    create_date = fields.Datetime("納品日", required=True)

    default_code = fields.Char(
        string='default_code', help="default_code from product record")

    # 商品を選んだら内部参照を表示する
    @api.onchange("product_id")
    def _onchange_default_code(self):
        print(self.product_id)
        self.default_code = self.product_id.default_code

    # @api.onchange("default_code")
    # def _onchange_product_id(self):
    #     print(self.product_id)
    #     self.product_id = self.product_id.name
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100



