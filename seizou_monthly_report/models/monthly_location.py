# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class seizou_monthly_location(models.Model):
    _name = 'seizou_monthly_location.location'
    _description = 'seizou_monthly_location.location'

    # 拠点
    location = fields.Many2one("seizou_monthly_report.monthly")
