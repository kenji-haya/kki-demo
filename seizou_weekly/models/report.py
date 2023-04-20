# -*- coding: utf-8 -*-

from odoo import _, models, fields, api
from datetime import datetime


# 製造部週間報告書
class seizou_weekly(models.Model):
    _name = 'seizou_weekly.report'
    _description = 'seizou_weekly.report'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    create_date = fields.Date(string="create_date", default=datetime.today())
    # author = fields.Char(string="author", required="True")
    author = fields.Many2one("hr.employee", string="member", required=True)
    # base_name = fields.Char(string="base_name")
    base_name = fields.Selection(
        [('one', '本社'), ('two', '摂津'), ('three', '厚木'), ('four', '沖縄')],
        "base_name", default='one', required=True)
    department = fields.Selection(
        [('one', '製袋'), ('two', 'スリッター'), ('three', 'すべて')],
        "department", required=True)
    start_date = fields.Date(string="start_date")
    end_date = fields.Date(string="end_date")
    comment = fields.Text(string="comment")
    file1 = fields.Binary(string="file1")
    file_name1 = fields.Char("file_name1")
    file2 = fields.Binary(string="   ")
    file_name2 = fields.Char("file_name2")
    file3 = fields.Binary(string="   ")
    file_name3 = fields.Char("file_name3")
    active = fields.Boolean(default=True)

    def archived_button(self):
        self.write({'active': False})

    def archive_button(self):
        self.write({"active": False})
        action = {'type': 'ir.actions.act_url',
                  'target': 'self',
                  'url': '/web#model=seizou_weekly.report&view_type=list'
                  }
        return action
