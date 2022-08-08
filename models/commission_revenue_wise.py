# -*- coding: utf-8 -*-
from odoo import models, fields


class CommissionRevenueWise(models.Model):
    _name = 'commission.revenue.wise'
    _description = 'Commission Revenue Wise'
    _rec_name = 'sequence'
    _order = 'sequence'

    sequence = fields.Integer(string='Sequence')
    commission_id = fields.Many2one('crm.commission', string='Commission ID')
    currency_id = fields.Many2one('res.currency',
                                  default=lambda self:
                                  self.env.user.company_id.currency_id.id,
                                  string='Currency')
    minimum_amount = fields.Float(string='Minimum Amount')
    maximum_amount = fields.Float(string='Maximum Amount')
    commission_rate = fields.Float(string='Commission Rate %')
