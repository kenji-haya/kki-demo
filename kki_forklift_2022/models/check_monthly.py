# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from datetime import datetime,timedelta
from odoo.exceptions import ValidationError
import pytz

class kki_forklift_check_monthly(models.Model):
    _name = 'kki_forklift.monthly'
    _description = 'kki_forklift.monthly'

    name_month = fields.Many2one("hr.employee", string="name", required=True)
    owner_id_month = fields.Many2one('res.users', 'owner_id', default=lambda self: self.env.user)
    check_date_month = fields.Date("check_date_month", required=True)
    lift_id = fields.Many2one("kki_forklift_2022.lift", "Forklift")
    defective_parts_im = fields.Binary("image")

    handle_check = fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default='one')

    fork_check1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default='one')
    fork_check2= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default='one')
    fork_check3= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default='one')
    fork_check4= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default='one')
    handle_1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")
    break_1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")
    horn_1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")
    volt_1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")
    oil_1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")

    remarks_2= fields.Char("remarks")
    alert_mes1 = fields.Boolean(string="Warning!!", store=True, tracking=True)

    @api.onchange("name_month")
    def _get_date(self):
        n_time = timedelta(hours=9)
        now_date = datetime.today() + n_time
        if self.name_month:
            self.check_date_month = now_date

    # 未実施項目があればalert_mesをTrueにする
    @api.model
    def create(self, values):
        for i in values.values():
            if i == 'one':
                values['alert_mes1'] = True
                break

        res = super(kki_forklift_check_monthly, self).create(values)
        return res

    # 最新のチェック日付を表示
    @api.constrains("check_date_month")
    def _get_last_date(self):
        if self.lift_id.last_check_date:
            if self.lift_id.last_check_date > self.check_date_month:
                print(f'print1:{self.lift_id.last_check_date}')
                print(self.lift_id.name)
            else:
                # print(f'print3:{self.name.name}')
                print(f'print{self.check_date_month}')
                self.env['kki_forklift_2022.lift'].search([('id', '=', self.lift_id._origin.id), ]).write({
                    'last_date_month': self.check_date_month,
                    'last_name_month': self.name_month.name,
                })
        self.env['kki_forklift_2022.lift'].search([('id', '=', self.lift_id._origin.id), ]).write({
            'last_date_month': self.check_date_month,
            'last_name_month': self.name_month.name,
        })

    #　未実施項目があればアラートを出す
    @api.constrains('alert_mes1')
    def constrains_no_check_warning(self):
        if self.alert_mes1:
            raise ValidationError(message="未実施項目があります。確認してください。")

    # 保存アクションの定義
    # @api.multi
    def action_save_and_confirm_month(self):
        # レコードを保存
        self.ensure_one()
        self.write(self._context.get('default_values', {}))

        # 確定画面への遷移アクションを返す
        return {
            'type': 'ir.actions.act_window',
            'name': 'Confirmation',
            'res_model': 'kki_forklift.monthly',  # 適切なモデル名に置き換える
            'view_mode': 'form',  # 遷移先がフォームビューの場合
            'view_type': 'form',
            'res_id': self.id,  # 保存したレコードのIDを指定
            'target': 'current',
        }