# -*- coding: utf-8 -*-
{
    'name': "Open Academy - JPM",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "jpm",
    'website': "www.odoo.com",
    'category': 'Demo',
    'version': '0.1',
    'depends': ['sale'],
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/views.xml',
        'views/sale_order_inherited_jpm.xml',
        'reports/sale_order_inherited_report.xml',
    ],
    'demo': [],
}