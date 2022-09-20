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
        string="商品区分", )


    # """ 仕様タブに入れる項目（仕様タブは一般情報タブの右隣に新規で作成する） """
    # 材料コード※本当はMany2one
    material_code = fields.Char("材料コード")
    # 内容量
    content_by_volume = fields.Integer("内容量")
    # 銘柄※本当はMany2one
    # brand = fields.Char("銘柄")

    # """ 仕様タブに入れる項目（仕様タブは一般情報タブの右隣に新規で作成する） """
    # 材料コード
    # material_code = fields.Char()
    # 内容量
    # content_by_volume = fields.Integer()
    # 銘柄※本当はMany2one
    # brand = fields.Char("銘柄")

    # 面付
    pagination = fields.Integer("面付",)
    # 出し方向
    way_of_paying = fields.Selection([
        ('1', '尻'),
        ('2', '頭'),
        ('3', 'なし'),
    ], default='',
        string="出し方向", required=True)
    # 厚さ
    thickness = fields.Integer("厚さ", default="")
    # 巾A
    width_A = fields.Integer("巾A")
    # 長さ
    pitch = fields.Integer("長さ")
    # 色数
    number_of_colors = fields.Integer("色数")

    """ 販売タブに入れる項目 """
    # 得意先※本当はMany2one

    customer_code = fields.Many2one("res.partner", string="得意先")
    # 品番
    stock_number = fields.Text("品番")

    warning = fields.Boolean(default=False)

    @api.model
    def create(self, values):
        print(values)
        for i in values.values():
            if values['thickness'] == 0:
                values['warning'] = True

        res = super(kki_product_additional_item, self).create(values)
        return res

    # @api.constrains("warning")
    # def value_pagination(self):
    #     for rec in self:
    #         print("あああ")
    #         print(rec)
    #         if rec.warning:
    #             raise ValidationError(message="未実施項目があります。確認してください。")



