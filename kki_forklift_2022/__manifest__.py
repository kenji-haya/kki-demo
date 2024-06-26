# -*- coding: utf-8 -*-
{
    'name': "kki_forklift",

    'summary': """
        fork lift management""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Enzantrades Inc,(k_eguchi)",
    'website': "http://www.enzantrades.co.jp",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'hr','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/forklift.xml',
        'views/size.xml',
        'views/check_history.xml',
        'views/check_monthly.xml',
        'views/place.xml',
        'views/templates.xml',
        'views/custom_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'kki_forklift_2022/static/src/css/custom_style.css',
        ],
        # デモモードでのみ読み込まれるデータ
        'demo': [
            'demo/demo.xml',
        ],
    },
}
