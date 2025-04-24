from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

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
    customer_code = fields.Char("Customer Code")
    tax_exempt_number = fields.Char("Tax Exempt Number")
    ship_via_code = fields.Char("Ship Via Code")
    first_sale_date = fields.Date("First Sale Date")
    last_sale_date = fields.Date("Last Sale Date")
    credit_holding_flag = fields.Boolean("Credit Holding Flag")
    credit_rating = fields.Char("Credit Rating")
    main_account = fields.Char("Main Account")
    sub_account = fields.Char("Sub Account")
    balance = fields.Char("Balance")