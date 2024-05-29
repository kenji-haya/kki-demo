# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_forklift_place(models.Model):
    _name = 'kki_forklift.place'
    _description = 'kki_forklift.place'

    name = fields.Char("name")