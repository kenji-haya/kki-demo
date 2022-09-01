# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class kki_forklift_check_history(models.Model):
    _name = 'kki_forklift.history'
    _description = 'kki_forklift.history'

    name = fields.Char("name")
    owner_id = fields.Many2one('res.users', 'owner_id', default=lambda self: self.env.user)
    check_date = fields.Date("check date", required="True", default=datetime.today())
    lift_id = fields.Many2one("kki_forklift.lift", "Forklift")
    image = fields.Binary("image")
    fork_1 = fields.Boolean("【フォーク】亀裂や曲がりはないか")
    back_1 = fields.Boolean("【バックレスト】亀裂・変形・取付部に緩みはないか")
    chain_1 = fields.Boolean("【チェーン】傷・ねじれがなく、張りが均等か")
    mast_1 = fields.Boolean("【マスト】上昇・下降・前後斜が円滑か")
    tire_1 = fields.Boolean("【タイヤ】損傷や異常摩耗がないか／ハブナットの緩み、脱落がないか")
    handle_1 = fields.Boolean("【ハンドル】著しい遊びまたはガタツキがないか")

