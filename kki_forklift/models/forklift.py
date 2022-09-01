# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_forklift(models.Model):
    _name = 'kki_forklift.lift'
    _description = 'kki_forklift.lift'

    name = fields.Char("name")
    image = fields.Binary("image")
    launch_day = fields.Date("Launch Day")
    vendor = fields.Many2one("res.partner", string="vendor")
    note = fields.Text("note")
    size = fields.Many2one("kki_forklift.size", string="size")
    check_history_ids = fields.One2many(
        comodel_name="kki_forklift.history",
        inverse_name="lift_id",
        string="check history")
    price = fields.Integer("price")

