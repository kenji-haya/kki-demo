# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta


class kki_forklift(models.Model):
    _name = 'kki_forklift.lift'
    _description = 'kki_forklift.lift'
    _inherit = ['mail.thread', 'mail.activity.mixin']

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
    history_count_2 = fields.Integer("test")
    history_count = fields.Integer(compute="_compute_check_history_count")

    def _compute_check_history_count(self):
        for rec in self:
            history_count = self.env['kki_forklift.history'].search_count([('lift_id', '=', rec.id)])
            rec.history_count = history_count