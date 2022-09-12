# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_product_additional_item_menu2(models.Model):
    _inherit = "product.template"

    menu_2 = fields.Many2one("kki_product_menu2.menu2", "カテゴリ")
    # menu_2 = fields.Char("カテゴリ")
