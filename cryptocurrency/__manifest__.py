# -*- coding: utf-8 -*-
{
    'name': 'Crypto-currencies',
    'version': '1.0',
    'summary': 'Manage crypto-currencies and convert',
    'description': """
Core mechanisms for the managing of crypto-currencies.
Allow a higher decimmal precicion.
Track the current value of all your assets
    """,
    'category': 'Accounting',
    'depends': ['decimal_precision', 'account'],
    'data': [
        'data/currency.xml',

        'views/asset.xml',
        'views/sync_wizard.xml',

        'report/assets_report_views.xml',
    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}