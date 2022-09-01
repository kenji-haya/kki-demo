# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_forklift_size(models.Model):
    _name = 'kki_forklift.size'
    _description = 'kki_forklift.size'

    name = fields.Char("name")
