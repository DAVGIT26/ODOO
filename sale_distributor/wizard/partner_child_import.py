# -*- coding: utf-8 -*-
from odoo import models, fields, _
from odoo.exceptions import UserError
import base64
import pandas as pd
from io import BytesIO

class PartnerChildImportWizard(models.TransientModel):
    _name = 'res.partner.child.import.wizard'
    _description = 'Import Child Contacts Wizard'

    file = fields.Binary(string="Excel File", required=True)
    filename = fields.Char(string="Filename")

    def action_import_child_contacts(self):
        if not self.file:
            raise UserError("Please upload a file.")
        data = base64.b64decode(self.file)
        df = pd.read_excel(BytesIO(data))
        if 'Customer ID' not in df.columns:
            raise UserError("Excel must contain 'Customer ID' columns.")
        for _, row in df.iterrows():
            parent_name = str(row['Customer ID']).strip()
            child_name = str(row['Contact First Name']).strip()
            if not parent_name:
                continue

            parent = self.env['res.partner'].search([('customer_number', '=', parent_name)], limit=1)
            if not parent:
                continue

            self.env['res.partner'].create({
                'name': child_name,
                'parent_id': parent.id,
                'type': 'contact'
            })
