# -*- coding: utf-8 -*-

from odoo import models,fields,api
from datetime import datetime


class kki_forklift_check_history(models.Model):
    _name = 'kki_forklift.history'
    _description = 'kki_forklift.history'

    name = fields.Char("name")
    owner_id = fields.Many2one('res.users','owner_id',default=lambda self:self.env.user)
    check_date = fields.Date("check date",required="True",default=datetime.today())
    lift_id = fields.Many2one("kki_forklift.lift","Forklift")
    image = fields.Binary("image")
    # fork_1= fields.Boolean("【フォーク】亀裂や曲がりはないか")
    fork_1= fields.Selection(
        [('one','未実施'),('two','点検済'),('three','不具合有')],"【フォーク】亀裂や曲がりはないか",default='one')
    # back_1= fields.Boolean("【バックレスト】亀裂・変形・取付部に緩みがないか")
    back_1= fields.Selection(
        [('one','未実施'),('two','点検済'),('three','不具合有')],"【バックレスト】亀裂・変形・取付部に緩みがないか",default='one')
    # chain_1= fields.Boolean("【チェーン】傷・ねじれがなく、張りが均等か")
    chain_1= fields.Selection(
        [('one','未実施'),('two','点検済'),('three','不具合有')],"【チェーン】傷・ねじれがなく、張りが均等か",default='one')
    # mast_1= fields.Boolean("【マスト】上昇・下降・前後傾が円滑か")
    mast_1= fields.Selection(
        [('one','未実施'),('two','点検済'),('three','不具合有')],"【マスト】上昇・下降・前後傾が円滑か",default='one')
    # tire_1= fields.Boolean("【タイヤ】損傷や異常摩耗がないか／ハブナットの緩み、脱落がないか")
    tire_1= fields.Selection(
        [('one','未実施'),('two','点検済'),('three','不具合有')],"【タイヤ】損傷や異常摩耗がないか／ハブナットの緩み、脱落がないか",default='one')
    handle_1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        '【ハンドル】著しい遊び又はガタツキがないか',
        default="one")
    break_1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        '【ブレーキペダル】ブレーキの効きが充分か',
        default="one")
    horn_1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        '【ホーン・バックブザー】正常に鳴るか',
        default="one")
    volt_1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        '【ボルトメーター】規定量か',
        default="one")
    oil_1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        '【冷却水・オイル・バッテリー液】規定量か。油や水が落ちていないか',
        default="one")
    remarks_1= fields.Char("remarks")

    fork_2= fields.Selection([('one','One'),('two','Two')],'Syllabus')
