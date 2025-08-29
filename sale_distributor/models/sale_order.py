from odoo import models, fields, api
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        order = super().create(vals)
        order._update_partner_sale_dates()
        return order

    def write(self, vals):
        res = super().write(vals)
        self._update_partner_sale_dates()
        return res

    def _update_partner_sale_dates(self):
        for order in self:
            if order.partner_id:
                today = fields.Date.today()
                partner = order.partner_id

                if not partner.first_sale_date:
                    partner.first_sale_date = today

                partner.last_sale_date = today


def action_confirm(self):
    res = super().action_confirm()
    self._update_partner_sale_dates()
    return res
