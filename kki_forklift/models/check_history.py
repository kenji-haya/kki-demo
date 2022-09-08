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
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        "【フォーク】亀裂や曲がりはないか", default='one')
    back_1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        "【バックレスト】亀裂・変形・取付部に緩みがないか", default='one')
    chain_1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        "【チェーン】傷・ねじれがなく、張りが均等か", default='one')
    mast_1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        "【マスト】上昇・下降・前後傾が円滑か", default='one')
    tire_1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        "【タイヤ】損傷や異常摩耗がないか／ハブナットの緩み、脱落がないか", default='one')
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
    alert_mes = fields.Boolean(string="Warning!!", compute='create', store=True, Tracking=True)


    # @api.model
    # def create(self, values):
    #     res = super(kki_forklift_check_history, self).create(values)
    #     print(self.fork_1)
    #     print(res)
    #     return res

    @api.model
    def create(self, values):
        alert = False
        for i in values.values():
            if i == 'one':
                # values['alert_mes'] = 1
                alert = True
        else:
            self.alert_mes = True

        if alert:
            values['alert_mes'] = True
        else:
            values['alert_mes'] = False

        res = super(kki_forklift_check_history, self).create(values)
        return res

    # @api.model
    # def save(self, values):
    #     alert = False
    #     print(values)
    #     for i in self._values.values():
    #         print(i)
    #         if i == 'one':
    #             # values['alert_mes'] = 1
    #             alert = True
    #     else:
    #         self.alert_mes = True
    #
    #     if alert:
    #         values['alert_mes'] = True
    #         print("check")
    #         return
    #     else:
    #         values['alert_mes'] = False
    #         return super(kki_forklift_check_history, self).save(values)




    # @api.depend()
    # def _create(self, alert):
    #     self.alert_mes = alert

        # res.update(
        #     crm_alias_prefix=alias.alias_name if alias else False,
        # )
        # return res

    # @api.model
    # def write(self, values):
    #     res = super(kki_forklift_check_history, self).write(values)
    #     print(self.lift_id)
    #     return res
