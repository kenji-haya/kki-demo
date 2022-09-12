# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_product_additional_item_brand(models.Model):
    _inherit = "product.template"

    brand = fields.Many2one("kki_product_brand.brand", "銘柄")
    # brand = fields.Char("銘柄")

