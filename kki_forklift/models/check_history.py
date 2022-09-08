# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from datetime import datetime
from odoo.exceptions import ValidationError


class kki_forklift_check_history(models.Model):
    _name = 'kki_forklift.history'
    _description = 'kki_forklift.history'

    name = fields.Char("name")
    owner_id = fields.Many2one('res.users','owner_id',default=lambda self:self.env.user)
    check_date = fields.Date("check date",required="True",default=datetime.today())
    lift_id = fields.Many2one("kki_forklift.lift","Forklift")
    image = fields.Binary("image")
    fork_1 = fields.Boolean("【フォーク】亀裂や曲がりはないか")
    back_1 = fields.Boolean("【バックレスト】亀裂・変形・取付部に緩みがないか")
    chain_1 = fields.Boolean("【チェーン】傷・ねじれがなく、張りが均等か")
    mast_1 = fields.Boolean("【マスト】上昇・下降・前後傾が円滑か")
    tire_1 = fields.Boolean("【タイヤ】損傷や異常摩耗がないか／ハブナットの緩み、脱落がないか")
    handle_1 = fields.Selection(
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

    # @api.model
    # def create(self, values):
    #     res = super(kki_forklift_check_history, self).create(values)
    #     print(self.lift_id)
    #     return

    @api.onchange("check_date")
    def _get_last_date(self):
        print("triger")
        if self.lift_id.last_check_date > self.check_date:
            print(self.lift_id.last_check_date)
        else:
            print(self.lift_id._origin.id)
            self.env['kki_forklift.lift'].search([('id', '=', self.lift_id._origin.id), ]).write({
                'last_check_date': self.check_date
            })
        self._origin.lift_id.last_check_date = self.check_date

    @api.constrains('name')
    def _check(self):
        print("test")
        for line in self:
            if not line.name:
                raise ValidationError(
                        _("input name")
                    )
            # if not line.secondary_uom_id and line.secondary_uom_price != 0.0:
            #     raise ValidationError(
            #         _("Please enter secondary UoM or remove the secondary UoM price.")
            #     )