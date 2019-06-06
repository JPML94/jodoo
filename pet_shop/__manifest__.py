# -*- coding: utf-8 -*-
{
    'name': "Pet Shop",

    'summary': """
        Keep track of everything related to your pets.""",

    'description': """
        This module provides a set of tools to keep track of everything in regards to your pets.

        Some examples are:
          - Pet vaccine tracker
          - Log important events in your pet's life
          - Track spending of food and accesories/toys
    """,

    'author': "jpm",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}