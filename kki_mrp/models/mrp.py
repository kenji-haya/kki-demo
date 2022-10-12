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

    product = fields.Char(
        string='product', compute="_cumpute_product_id"
    )

    # 商品を選んだら内部参照を表示する
    @api.onchange("product_id")
    def _onchange_default_code(self):
        if self .default_code:
            self.default_code = self.product_id.default_code

    # デフォルトコードが更新されたら商品を検索してプロダクトに代入する
    @api.onchange("default_code")
    def _cumpute_product_id(self):
        for rec in self:
            if rec.default_code:
                product = self.env['product.product'].search([('default_code', '=', rec.default_code)])
                if product:
                    print(rec.product_id)
                    rec.product_id = product
                else:
                    rec.product_id = False

            # rec.product_id = product

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100



