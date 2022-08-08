# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CrmCommission(models.Model):
    _name = 'crm.commission'
    _description = 'CRM Commission'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(default=True, string='Active')
    from_date = fields.Date(string='From Date')
    to_date = fields.Date(string='To Date')
    type = fields.Selection([('product_wise', 'Product wise'),
                             ('revenue_straight', 'Revenue Wise-Straight'),
                             ('revenue_graduated', 'Revenue Wise-Graduated')],
                            string='Type', default='product_wise')
    commission_rate = fields.Float(string='Commission Rate')
    product_wise_ids = fields.One2many(
        'commission.product.wise', 'commission_id', string='Product Wise '
                                                           'ID')
    revenue_wise_ids = fields.One2many(
        'commission.revenue.wise', 'commission_id',
        string='Revenue-Wise ID')
