# -*- coding: utf-8 -*-
{
    'name': "alquiler videojuegos",

    'summary': """
        En este modulo podemos asignar a diferentes clientes
        """,

    'description': """
        Este modulo fue desarrollado para gestionar los alquileres
    """,

    'author': "Bryan Steven",
    'website': "http://infsalinas.sytes.net:10190/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True ,
}
