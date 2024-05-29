# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from datetime import datetime,timedelta
from odoo.exceptions import ValidationError
import pytz
class kki_forklift_check_monthly(models.Model):
    _name = 'kki_forklift.monthly'
    _description = 'kki_forklift.monthly'
    name_month = fields.Many2one("hr.employee", string="name", required=True,
                                 default=lambda self: self._get_default_inspector())
    owner_id_month = fields.Many2one('res.users', 'owner_id', default=lambda self: self.env.user)
    check_date_month = fields.Date("check_date_month", required=True)
    lift_id = fields.Many2one("kki_forklift_2022.lift", "Forklift")
    defective_parts_im = fields.Binary("image")

    handle_check1 = fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default='one')
    handle_check2 = fields.Selection(
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

    hydraulic1= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")
    hydraulic2= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")
    hydraulic3= fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")
    hydraulic4 = fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")
    hydraulic5 = fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")
    hydraulic6 = fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")

    running1 = fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")
    running2 = fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")

    safety1 = fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")
    safety2 = fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")
    safety3 = fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")
    safety4 = fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")
    safety5 = fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")
    safety6 = fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")

    brake1 = fields.Selection(
        [('one', '未実施'), ('two', '点検済'), ('three', '不具合有')],
        default="one")

    comp1 = fields.Selection(
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
        if self.lift_id.last_date_month:
            if self.lift_id.last_date_month > self.check_date_month:
                print(f'print1:{self.lift_id.last_date_month}')
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
    @api.model
    def _get_default_inspector(self):
        # 最終点検日のレコード番号を取得
        last_fork = self.env['kki_forklift.monthly'].search([], order='check_date_month desc', limit=1)
        print(f'last_fork:{last_fork.name_month.name}')
        print(f'last_fork:{last_fork.check_date_month}')
        if last_fork.name_month:
            print(f'last_fork.name:{last_fork.name_month}')
            print(f'last_fork.nametype:{type(last_fork.id)}')
            return last_fork.name_month
        return False
    # 未実施項目があればアラートを出す
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