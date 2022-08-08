# -*- coding: utf-8 -*-
from odoo import models, fields


class CRMTeamInherit(models.Model):
    _inherit = 'crm.team'

    commission_id = fields.Many2one('crm.commission', string='Commission')
