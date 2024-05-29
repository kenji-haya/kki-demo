# -*- coding: utf-8 -*-
import base64
import os

from odoo import _, api, fields, models
from datetime import datetime,timedelta
from odoo.exceptions import ValidationError
import pytz

# from odoo.odoo.exceptions import UserError


class kki_forklift_check_history(models.Model):
    _name = 'kki_forklift.history'
    _description = 'kki_forklift.history'

    name = fields.Many2one("hr.employee", string="name", required=True,
                           default=lambda self: self._get_default_inspector_history())
    owner_id = fields.Many2one('res.users', 'owner_id', default=lambda self: self.env.user)
    check_date = fields.Date("check date", required=True)
    lift_id = fields.Many2one("kki_forklift_2022.lift", "Forklift")
    defective_history_im = fields.Binary("image")
    defective_history_im_path = fields.Char("Image Path", readonly=True)  # 画像パスのフィールドを追加
    image_url = fields.Char("Image URL", compute="_get_image_url")

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

    @api.model
    def _get_default_inspector_history(self):
        # 最終点検日のレコード番号を取得
        last_fork = self.env['kki_forklift.history'].search([], order='check_date desc', limit=1)
        print(f'last_fork:{last_fork.name.name}')
        print(f'last_fork:{last_fork.check_date}')
        if last_fork.name:
            print(f'last_fork.name:{last_fork.name}')
            print(f'last_fork.nametype:{type(last_fork.id)}')
            return last_fork.name
        return False

    @api.model
    def create(self, vals):
        record = super(kki_forklift_check_history, self).create(vals)
        if 'defective_history_im' in vals:
            record._save_image_to_filesystem()
        return record

    def write(self, vals):
        result = super(kki_forklift_check_history, self).write(vals)
        if 'defective_history_im' in vals:
            self._save_image_to_filesystem()
        return result

    def _save_image_to_filesystem(self):
        for record in self:
            if record.defective_history_im:
                # 保存先のディレクトリを指定
                save_dir = r'\Odoo_kki\addons\kki-demo\kki_forklift_2022\static\images'
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)

                # ファイル名を設定
                if record.name:
                    file_name = f"/{record.name.id}_{record.id}.png"
                else:
                    file_name = f"/{record.id}.png"

                file_path = os.path.join(save_dir, file_name)

                try:
                    # バイナリデータをデコードしてファイルに書き込み
                    with open(file_path, 'wb') as file:
                        file.write(base64.b64decode(record.defective_history_im))

                    # 必要に応じて、データベース内のフィールドをクリアするなどの操作を行う
                    record.defective_history_im = False
                except Exception as e:
                    raise UserError(f"Failed to save image: {e}")

    @api.depends('defective_history_im_path')
    def _get_image_url(self):
        for record in self:
            if record.defective_history_im_path:
                # WindowsパスをWeb URLに変換
                # パスのセパレータを適切に変換
                image_path = record.defective_history_im_path.replace('\\', '/')
                record.image_url = f'/kki_forklift/static/images/{image_path}'
                print(record.image_url)
            else:
                record.image_url = False


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