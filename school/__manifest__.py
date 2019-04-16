# -*- coding: utf-8 -*-
{
    'name': "school",
    'summary': """
      Quick module for student records for practice""",
    'description': """
    Record Student Information
    """,
    'author': "JPML",
    'website': "https://jpml.online",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],
    'data': ['security/ir.model.access.csv', 'views/student_view.xml'],
    'installable': True,
    'application': False,
    'auto_install': False,
}