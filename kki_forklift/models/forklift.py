# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime, timedelta
from odoo.exceptions import AccessError, UserError
from dateutil.relativedelta import relativedelta


class kki_forklift(models.Model):
    _name = 'kki_forklift.lift'
    _description = 'kki_forklift.lift'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("name")
    image = fields.Binary("image")
    launch_day = fields.Date("Launch Day")
    vendor = fields.Many2one("res.partner", string="vendor")
    note = fields.Text("note")
    size = fields.Many2one("kki_forklift.size", string="size")
    check_history_ids = fields.One2many(
        comodel_name="kki_forklift.history",
        inverse_name="lift_id",
        string="check history")
    price = fields.Integer("price")
    history_count_2 = fields.Integer("test")
    history_count = fields.Integer(compute="_compute_check_history_count")
    owner_id = fields.Many2one("kki_forklift.history", string="owner_id")
    last_check_date = fields.Date('last_check_date')
    next_date = fields.Date('next_date', compute="_next_date")
    annual_inspection= fields.Date('annual_inspection', compute="_next_inspection")
    active = fields.Boolean(default=True)

    def _compute_check_history_count(self):
        for rec in self:
            history_count = self.env['kki_forklift.history'].search_count([('lift_id', '=', rec.id)])
            rec.history_count = history_count

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

    # def delete_form(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'kki_forklift.history',
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'target': 'current',
    #         'context': {
    #             # 'default_id': self.id,
    #             # 'default_check_date': datetime.today(),
    #             'default_lift_id': self.id,
    #             'default_owner_id': self.env.user.id,
    #         }
    #     }
    #

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

    @api.depends('last_check_date')
    def _next_date(self):
        # 日程がない場合の処理をここで判定させる
        for rec in self:
            if rec.last_check_date:
                rec.next_date = rec.last_check_date + timedelta(days=30)
            else:
                rec.next_date =""

    @api.depends('launch_day')
    def _next_inspection(self):
        # 日程がない場合の処理をここで判定させる
        for rec in self:
            if rec.launch_day:
                rec.annual_inspection = rec.launch_day + timedelta(days=365)
            else:
                rec.annual_inspection =""

