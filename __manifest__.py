# -*- coding: utf-8 -*-
{
    'name': "Commission Plan",

    'summary': """
        Helps to manage commission plans""",

    'description': """
        Description
    """,

    'author': "Minions 6",

    'version': '15.0.1.0',
    'depends': ['base', 'crm', 'product', 'sale_management'],

    'data': ['security/ir.model.access.csv',
             'views/crm_commission_views.xml',
             'views/crm_inherits_views.xml',
             'views/crm_commission_menu_items.xml',
             ],
}
