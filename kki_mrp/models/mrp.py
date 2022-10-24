# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_mrp(models.Model):
    _inherit = "mrp.production"
    # _name = 'kki_mrp.kki_mrp'
    # _description = 'kki_mrp.kki_mrp'
    # order_date = fields.Datetime("納品日", required=True)
    kcreate_date = fields.Date("手配日", required=True)
    default_code = fields.Char(
        string='default_code', help="default_code from product record")
    menu_1 = fields.Char(
        string="Factory", help="menu_1 from product record")

    # arrival_day = fields.Char(
    #     string='arrival_day', help="date_deadline from stock_move record",compute='_arrival_day')
    #
    arrival_day = fields.Char(
        string='arrival_day', help="date_deadline from stock_move record")



    # 商品を選んだら内部参照を表示する
    @api.onchange("product_id")
    def _onchange_default_code(self):
        # if self.default_code:
            self.menu_1 = self.product_id.menu_1.name
            self.default_code = self.product_id.default_code


    # デフォルトコードが更新されたら商品を検索してプロダクトに代入する
    @api.onchange("default_code")
    def _compute_product_id(self):
        for rec in self:
            if rec.default_code:
                product = self.env['product.product'].search([('default_code', '=', rec.default_code)])
                print(f'product:{product[0]}')
                if product:
                    rec.product_id = product[0]
            else:
                rec.product_id = ""


    # デフォルトコードが更新されたら商品を検索してプロダクトに代入する
    # def _arrival_day(self):
    #     for rec in self:
    #         if rec.arrival_day:
    #             date = self.env['stock.move'].search([('date_deadline', '=', rec.date_deadline)])
    #             print(date)
    #             if date:
    #                 rec.product_id = date
    #         else:
    #             rec.product_id = ""



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100



