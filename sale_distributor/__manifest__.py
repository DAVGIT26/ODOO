{
    'name': 'Sale Distributor Integration',
    'version': '17.0.1.0.0',
    'summary': 'Integrate distributor APIs for product pricing and availability in sale orders.',
    'description': """
        This module integrates with multiple distributor APIs (Ingram Micro, TD Synnex, and D&H)
        to fetch product pricing and availability. Users can select the best option and add it 
        directly to the sale order line.
    """,
    'category': 'Sales',
    'author': 'Acespritech Solutions Pvt. Ltd.',
    'website': 'www.acespritech.com',
    'depends': ['sale_management', 'purchase', 'account'],
    'data': [
        # 'views/delivery_carrier.xml',
        'views/account_payment_term.xml',
        'data/data.xml',
        'views/res_partner.xml',
        'views/account_tax.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}