# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class kki_forklift_check_history(models.Model):
    _name = 'kki_forklift.history'
    _description = 'kki_forklift.history'

    name = fields.Char("name")
    check_date = fields.Date("check date", required="True", default=datetime.today())
    lift_id = fields.Many2one("kki_forklift.lift", "Forklift")
    image = fields.Binary("image")
    fork_1 = fields.Boolean("【フォーク】亀裂や曲がりはないか")
    back_1 = fields.Boolean("【バックレスト】")
    chain_1 = fields.Boolean("【チェーン】")
    mast_1 = fields.Boolean("【マスト】")
    tire_1 = fields.Boolean("【タイヤ】")
    handle_1 = fields.Boolean("【ハンドル】")
