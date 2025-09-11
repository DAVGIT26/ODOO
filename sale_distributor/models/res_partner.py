# -*- coding: utf-8 -*-
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    type = fields.Selection(selection_add=[('a', 'A'),('b', 'B'),('c', 'C')])
    contact_1 = fields.Char("Contact 1")
    contact_2 = fields.Char("Contact 2")
    terms_code = fields.Char("Terms Code")
    type_of_partner = fields.Char("Type")
    fax = fields.Char("Fax")
    comment = fields.Char("Comment")

    # Vendor data fields
    vendor_code = fields.Char("Vendor Code")
    ap_vendor_number = fields.Char("AP Vendor Number")

    # Customer data fields
    customer_number = fields.Char("Customer Number")
    tax_exempt_number = fields.Char("Tax Exempt Number")
    ship_to_number = fields.Char("Ship To Number")
    ship_via_code = fields.Many2one(comodel_name='delivery.carrier', string='Ship Code')
    tax_code = fields.Char(comodel_name='account.tax', string='Tax Code')
    first_sale_date = fields.Date("First Sale Date")
    last_sale_date = fields.Date("Last Sale Date")
    credit_holding_flag = fields.Boolean("Credit Holding Flag")
    credit_rating = fields.Char("Credit Rating")
    main_account = fields.Char("Main Account")
    sub_account = fields.Char("Sub Account")
    balance = fields.Char("Balance")