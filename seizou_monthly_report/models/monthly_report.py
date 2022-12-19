# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class seizou_monthly_report(models.Model):
    _name = 'seizou_monthly_report.monthly'
    _description = 'seizou_monthly_report.monthly'

    # レコード番号
    record_num = fields.Many2one('id', string="record_num")
    # 作成日時
    create_date = fields.Datetime("create_date", default=datetime.now())
    # 作成者
    member = fields.Many2one("hr.employee", string="member")
    # 拠点
    location = fields.Many2one('seizou_monthly_location.location', string="location")
    # 月度
    monthly = fields.Many2one()
    # 関連レコード一覧
    record_data = fields.Binary("record_data")
    # 関連レコード一覧のファイルネーム
    record_name = fields.Char('record_name')
    # コメント
    comment = fields.Char()
    # 月報添付
    file_data = fields.Binary("file_data")
    # 月報添付のファイルネーム
    file_name = fields.Char('file_name')

