# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    currency_id = fields.Many2one('res.currency',
                                  default=lambda self:
                                  self.env.user.company_id.currency_id.id,
                                  string='Currency')
    commission = fields.Float(compute='_compute_commission',
                              string='Commission', readonly=True)

    @api.depends('order_line.price_subtotal')
    def _compute_commission(self):
        self.commission = 0

        def _commission_calculation(self, commission):
            if commission.type == 'product_wise':
                for rec in self.order_line:
                    if rec.product_id:
                        commission_product = commission.product_wise_ids.filtered(
                            lambda r: r.product_id == rec.product_id)
                        commission_category = commission.product_wise_ids.filtered(
                            lambda r: r.category_id ==
                                      rec.product_id.categ_id)
                        print(commission_product.product_id, rec.product_id, commission_category)

                        def value(commission):
                            commission_amt = rec.price_subtotal * \
                                     commission.commission_rate
                            if commission_amt < commission.maximum_commission:
                                self.commission += commission_amt
                            else:
                                self.commission += commission.maximum_commission
                        if commission_product:
                            value(commission_product)
                        elif commission_category:
                            value(commission_category)
                        print(self.commission)
            elif commission.type == 'revenue_straight':
                self.commission = self.amount_total * commission.commission_rate
            elif commission.type == 'revenue_graduated':
                total = self.amount_total
                commission_amount = 0
                for line in commission.revenue_wise_ids:
                    if line.minimum_amount < total < line.maximum_amount or \
                            line.maximum_amount <= total:
                        mean = (line.minimum_amount +
                                line.maximum_amount) / 2
                        commission_amount += mean * line.commission_rate
                        total -= line.maximum_amount
                self.commission = commission_amount

        commission = self.user_id.commission_id
        team_commission = self.team_id.commission_id
        if commission:
            _commission_calculation(self, commission)
        elif team_commission:
            _commission_calculation(self, team_commission)
