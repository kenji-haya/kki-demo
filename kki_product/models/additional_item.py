# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError



class kki_product_additional_item(models.Model):
    _inherit = "product.template"

    # """ 販売可購買可の隣に入れる項目 """
    # 商品区分
    commodity_classification = fields.Selection([
        ('1', '加工'),
        ('2', '丸投'),
        ('3', '材料'),
        ('4', '仕入'),
        ('5', '半製品'),
    ], default='',
        string="商品区分", required=True)




    # """ 仕様タブに入れる項目（仕様タブは一般情報タブの右隣に新規で作成する） """
    # 材料コード※本当はMany2one
    material_code = fields.Char("材料コード", default='', required=True)

    # 内容量
    # content_by_volume = fields.Integer("内容量", default=666)
    content_by_volume = fields.Char("内容量", default='', required=True)

    # 面付
    # pagination = fields.Integer("面付", default=666)
    pagination = fields.Char("面付", default="", required=True)

    # 出し方向
    way_of_paying = fields.Selection([
        ('1', '尻'),
        ('2', '頭'),
        ('3', 'なし'),
    ], default='',
        string="出し方向", required=True)

    # 厚さ
    # thickness = fields.Integer("厚さ", default=666)
    thickness = fields.Char("厚さ", default='', required=True)

    # 巾A
    # width_A = fields.Integer("巾A", default=666)
    width_A = fields.Char("巾A", default='', required=True)

    # 長さ
    # pitch = fields.Integer("長さ", default=666)
    pitch = fields.Char("長さ", default='', required=True)

    # 色数
    # number_of_colors = fields.Integer("色数", default=666)
    number_of_colors = fields.Char("色数", default='', required=True)

    """ 販売タブに入れる項目 """
    # 得意先※本当はMany2one

    customer_code = fields.Many2one("res.partner", string="得意先", required= True)
    # 品番
    stock_number = fields.Text("品番", default='', required=True)






