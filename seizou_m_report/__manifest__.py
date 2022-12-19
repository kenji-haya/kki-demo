# -*- coding: utf-8 -*-
{
    'name': "seizou_m_report",

    'summary': """
        Manufacturing Department Monthly Report Management Application""",

    'description': """
        Used to record monthly reports and attach past weekly reports
    """,

    'author': "KKI Corporation Karasawa",
    'website': "https://www.v-kki.co.jp",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/seizou_m_report.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
