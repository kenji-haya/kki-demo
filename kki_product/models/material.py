# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_product_material(models.Model):
    _name = 'product.material'
    _description = 'kki_product_material'

    name = fields.Char(string='name')
