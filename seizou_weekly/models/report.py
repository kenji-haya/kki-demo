# -*- coding: utf-8 -*-

from odoo import _, models, fields, api
from datetime import datetime


# 製造部週間報告書
class seizou_weekly(models.Model):
    _name = 'seizou_weekly.report'
    _description = 'seizou_weekly.report'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    create_date = fields.Date(string="create_date", default=datetime.today())
    author = fields.Char(string="author")
    base_name = fields.Char(string="base_name")
    department = fields.Char(string="department")
    start_date = fields.Date(string="start_date")
    end_date = fields.Date(string="end_date")
    comment = fields.Text(string="comment")
    file = fields.Binary(string="file")
    file_name = fields.Char(string='file_name')
    file1 = fields.Binary(string="   ")
    file_name1 = fields.Char("file_name1")
    file2 = fields.Binary(string="   ")
    file_name2 = fields.Char("file_name2")
    file3 = fields.Binary(string="   ")
    file_name3 = fields.Char("file_name3")


