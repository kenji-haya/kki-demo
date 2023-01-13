# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class seizou_monthly_report(models.Model):
    _name = 'seizou_monthly_report.monthly'
    _description = 'seizou_monthly_report.monthly'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # レコード番号
    # record_num = fields.Boolean("id")
    # 作成日時
    create_date = fields.Datetime("create_date", default=datetime.now(), readonly=True)
    # 作成者
    member = fields.Many2one("hr.employee", string="member", required=True)
    # 拠点
    # 拠点
    location = fields.Selection(
        [('one', '本社'), ('two', '摂津'), ('three', '厚木'), ('four', '沖縄')],
        "location", default='one', required=True)
    # 月度
    monthly = fields.Selection(
        [('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'),
         ('seven', '7'), ('eight', '8'), ('nine', '9'), ('ten', '10'), ('eleven', '11'), ('twelve', '12')],
        "monthly", default='one', required=True)
    # 関連レコード一覧1
    # record_data_1 = fields.Binary("record_data")
    # 関連レコード一覧のファイルネーム1
    # record_name_1 = fields.Char('record_name')
    # 関連レコード一覧2
    # record_data_2 = fields.Binary("record_data")
    # 関連レコード一覧のファイルネーム2
    # record_name_2 = fields.Char('record_name')
    # 関連レコード一覧3
    # record_data_3 = fields.Binary("record_data")
    # 関連レコード一覧のファイルネーム3
    # record_name_3 = fields.Char('record_name')
    # 関連レコード一覧4
    # record_data_4 = fields.Binary("record_data")
    # 関連レコード一覧のファイルネーム4
    # record_name_4 = fields.Char('record_name')
    # 関連レコード一覧5
    # record_data_5 = fields.Binary("record_data")
    # 関連レコード一覧のファイルネーム5
    # record_name_5 = fields.Char('record_name')


    # コメント
    comment = fields.Char()
    # 月報添付
    file_data = fields.Binary("file_data", required=True)
    # 月報添付のファイルネーム
    file_name = fields.Char('file_name', required=True)

