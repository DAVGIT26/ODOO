from odoo import models, fields


class AccountTax(models.Model):
    _inherit = 'account.tax'

    sale_tax_code = fields.Char("Sales Tax Code")