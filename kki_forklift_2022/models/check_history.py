# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from datetime import datetime,timedelta
from odoo.exceptions import ValidationError
import pytz

class kki_forklift_check_history(models.Model):
    _name = 'kki_forklift.history'
    _description = 'kki_forklift.history'

    name = fields.Many2one("hr.employee", string="name", required=True,
                           default=lambda self: self._get_default_inspector_history())
    owner_id = fields.Many2one('res.users', 'owner_id', default=lambda self: self.env.user)
    check_date = fields.Date("check date", required=True)
    print(check_date)

    lift_id = fields.Many2one("kki_forklift_2022.lift", "Forklift")
    defective_parts_im = fields.Binary("image")

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
    alert_mes = fields.Boolean(string="Warning!!", store=True, tracking=True)

    @api.onchange("name")
    def _get_date(self):
        n_time = timedelta(hours=9)
        now_date = datetime.today() + n_time
        if self.name:
            self.check_date = now_date

    # 未実施項目があればalert_mesをTrueにする
    @api.model
    def create(self, values):
        for i in values.values():
            if i == 'one':
                values['alert_mes'] = True
                break

        res = super(kki_forklift_check_history, self).create(values)
        return res

    # 最新のチェック日付を表示
    @api.constrains("check_date")
    def _get_last_date(self):
        if self.lift_id.last_check_date:
            if self.lift_id.last_check_date > self.check_date:
                print(f'print1:{self.lift_id.last_check_date}')
                print(self.lift_id.name)
            else:
                # print(f'print3:{self.name.name}')
                print(f'print{self.check_date}')
                self.env['kki_forklift_2022.lift'].search([('id', '=', self.lift_id._origin.id), ]).write({
                    'last_check_date': self.check_date,
                    'last_check_name': self.name.name,
                })
        self.env['kki_forklift_2022.lift'].search([('id', '=', self.lift_id._origin.id), ]).write({
            'last_check_date': self.check_date,
            'last_check_name': self.name.name,
        })

    @api.onchange('lift_id')
    def _onchange_lift_id(self):
        if self.lift_id:
            self.name = self._get_default_inspector(self.lift_id)
        else:
            self.name = False

    def _get_default_inspector_history(self, lift_record=None):
        # If lift_record is not provided, try to fetch the default one from the context or return False
        if not lift_record:
            lift_record = self.env.context.get('default_lift_id')
            if lift_record:
                lift_record = self.env['kki_forklift_2022.lift'].browse(lift_record)

        if lift_record and lift_record.last_check_name:
            # Search for the hr.employee with the matching name
            employee = self.env['hr.employee'].search([('name', '=', lift_record.last_check_name)], limit=1)
            return employee.id if employee else False
        return False

    #　未実施項目があればアラートを出す
    @api.constrains('alert_mes')
    def constrains_no_check_warning(self):
        if self.alert_mes:
            raise ValidationError(message="未実施項目があります。確認してください。")

    # 保存アクションの定義
    # @api.multi
    def action_save_and_confirm(self):
        # レコードを保存
        self.ensure_one()
        self.write(self._context.get('default_values', {}))

        # 確定画面への遷移アクションを返す
        return {
            'type': 'ir.actions.act_window',
            'name': 'Confirmation',
            'res_model': 'kki_forklift.history',  # 適切なモデル名に置き換える
            'view_mode': 'form',  # 遷移先がフォームビューの場合
            'view_type': 'form',
            'res_id': self.id,  # 保存したレコードのIDを指定
            'target': 'current',
        }