# -*- coding: utf-8 -*-
from odoo import models, fields


class UsersInherit(models.Model):
    _inherit = 'res.users'

    commission_id = fields.Many2one('crm.commission', string='Commission')
