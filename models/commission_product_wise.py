# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CommissionProductWise(models.Model):
    _name = 'commission.product.wise'
    _description = 'Commission Product Wise'
    _rec_name = 'product_id'

    commission_id = fields.Many2one('crm.commission', string='Commission ID')
    category_id = fields.Many2one('product.category', string='Product Category')
    product_id = fields.Many2one('product.product', string='Product')
    commission_rate = fields.Float(string='Commission Rate %')
    currency_id = fields.Many2one('res.currency',
                                  default=lambda self:
                                  self.env.user.company_id.currency_id.id,
                                  string='Currency')
    maximum_commission = fields.Float(string='Maximum Commission Amount')

    @api.onchange("category_id")
    def _onchange_category_id(self):
        self.product_id = False
