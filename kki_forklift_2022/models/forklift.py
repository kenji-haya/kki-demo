# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import AccessError, UserError
from dateutil.relativedelta import relativedelta


class kki_forklift_2022(models.Model):
    _name = 'kki_forklift_2022.lift'
    _description = 'kki_forklift_2022.lift'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("name")
    image = fields.Binary("image")
    place_possession = fields.Many2one("kki_forklift.place", string="place")
    launch_day = fields.Date("Launch Day")
    vendor = fields.Many2one("res.partner", string="vendor")
    note = fields.Text("note")
    size = fields.Many2one("kki_forklift.size", string="size")
    check_history_ids = fields.One2many(
        comodel_name="kki_forklift.history",
        inverse_name="lift_id",
        string="check history")
    check_monthly_ids = fields.One2many(
        comodel_name="kki_forklift.monthly",
        inverse_name="lift_id",
        string="check monthly")
    price = fields.Integer("price")
    history_count_2 = fields.Integer("test")
    history_count = fields.Integer(compute="_compute_check_history_count")
    owner_id = fields.Many2one("kki_forklift.history", string="owner_id")

    # 日次点検用
    last_check_date = fields.Date('last_check_date')
    last_check_name = fields.Char('last_check_name')
    # 月次点検用
    last_date_month = fields.Date('last_date_month')
    last_name_month = fields.Char('last_name_month')
    history_cnt_month = fields.Integer(compute="_compute_check_month_count")

    annual_inspection = fields.Date('annual_inspection', compute="_next_inspection")

    active = fields.Boolean(default=True)

    battery_replace_day = fields.Date('battery_check_date')

    next_inspect_day = fields.Date('inspect_day', compute="_inspect_day")

    # 日次点検の点検回数を取得
    def _compute_check_history_count(self):
        for rec in self:
            history_count = self.env['kki_forklift.history'].search_count([('lift_id', '=', rec.id)])
            rec.history_count = history_count

    # 月次点検回数取得
    def _compute_check_month_count(self):
        for rec in self:
            history_count_month = self.env['kki_forklift.monthly'].search_count([('lift_id', '=', rec.id)])
            rec.history_cnt_month = history_count_month

    # 『日次点検』ボタンが押されたら日次点検シートへ遷移する
    def create_check(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'kki_forklift.history',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                # 'default_id': self.id,
                # 'default_check_date': datetime.today(),
                'default_lift_id': self.id,
                'default_owner_id': self.env.user.id,
            }
        }

    # 『月次点検』ボタンが押されたら、月次点検シートへ遷移する
    def monthly_check(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'kki_forklift.monthly',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                # 'default_id': self.id,
                # 'default_check_date': datetime.today(),
                'default_lift_id': self.id,
                'default_owner_id': self.env.user.id,
            }
        }

    # アーカイブボタンが押されたらアーカイブする
    def archived_button(self):
        self.write({'active': False})

    def archive_button(self):
        self.write({"active": False})
        # action = {
        #     'type': 'ir.actions.act_window',
        #     'name': "lift.kanban",
        #     'res_model': 'kki_forklift.lift',
        #     'view_mode': 'kanban',  # list
        # }

        action = {'type': 'ir.actions.act_url',
                  'target': 'self',
                  'url': '/web#model=kki_forklift.lift&view_type=kanban'
                  }
        return action

    def action_view_check(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'history',
            'res_model': 'kki_forklift.history',
            'domain': [('lift_id', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
            'context': {
                'default_lift_id': self.id,
                'default_owner_id': self.env.user.id,
            }
        }

    # @api.depends('last_check_date')
    # def _next_date(self):
    #     # 日程がない場合の処理をここで判定させる
    #     for rec in self:
    #         if rec.last_check_date:
    #             rec.next_date = rec.last_check_date + timedelta(days=30)
    #         else:
    #             rec.next_date =""

    @api.depends('launch_day')
    def _next_inspection(self):
        # 日程がない場合の処理をここで判定させる
        for rec in self:
            if rec.launch_day:
                rec.annual_inspection = rec.launch_day + timedelta(days=365)
            else:
                rec.annual_inspection =""

    # # 年次点検の日付検索
    # @api.depends('next_inspect_day')
    # def _inspect_day(self):
    #     # 日程がない場合の処理をここで判定させる
    #     print(timedelta(days=365))
    #     for rec in self:
    #         if rec.next_inspect_day:
    #             rec.next_inspect_day = datetime.today() + timedelta(days=365)
    #         else:
    #             rec.next_inspect_day = datetime.today() + timedelta(days=365)

    # 年次点検の日付検索(一年後を提示)
    @api.depends('next_inspect_day')
    def _inspect_day(self):
        # 日程がない場合の処理をここで判定させる
        # print(timedelta(days=365))
        for rec in self:
            print(rec.next_inspect_day)
            if rec.next_inspect_day:
                print(1)
                pass
            else:
                print(2)
                rec.next_inspect_day = datetime.today() + timedelta(days=365)


    # @api.depends('last_check_date')
    # def _next_date(self):
    #     # 日程がない場合の処理をここで判定させる
    #     for rec in self:
    #         if rec.last_check_date:
    #             rec.next_date = rec.last_check_date + timedelta(days=30)
    #         else:
    #             rec.next_date =""
