# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_product_additional_item_menu1(models.Model):
    _inherit = "product.template"

    menu_1 = fields.Many2one("kki_product_menu1.menu1", "工場名")
    # menu_1 = fields.Char("工場名")
