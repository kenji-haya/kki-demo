# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_product_additional_item(models.Model):
    _inherit = "product.template"

    """ 販売可購買可の隣に入れる項目 """
    # 商品区分
    commodity_classification = fields.Selection([
        ('1', '加工'),
        ('2', '丸投'),
        ('3', '材料'),
        ('4', '仕入'),
        ('5', '半製品'),
    ], default='',
        string="商品区分", )
    # メニュー1※本当はMany2one
    menu_1 = fields.Char("工場名")
    # メニュー2※本当はMany2one
    menu_2 = fields.Char("カテゴリ")

    """ 仕様タブに入れる項目（仕様タブは一般情報タブの右隣に新規で作成する） """
    # 材料コード※本当はMany2one
    material_code = fields.Char("材料コード")
    # 内容量
    content_by_volume = fields.Integer("内容量")
    # 銘柄※本当はMany2one
    brand = fields.Char("銘柄")
    # 面付
    pagination = fields.Integer("面付")
    # 出し方向
    way_of_paying = fields.Selection([
        ('1', '尻'),
        ('2', '頭'),
        ('3', 'なし'),
    ], default='',
        string="出し方向", )
    # 厚さ
    thickness = fields.Integer("厚さ")
    # 巾A
    width_A = fields.Integer("巾A")
    # 長さ
    pitch = fields.Integer("長さ")
    # 色数
    number_of_colors = fields.Integer("色数")

    """ 販売タブに入れる項目 """
    # 得意先※本当はMany2one
    customer_code = fields.Char("得意先")
    # 品番
    memo = fields.Text("品番")
