# -*- coding: utf-8 -*-
{
    'name': 'Hotel Chain Information',
    'summary': """Manage your Hotel information""",
    'description': """Hotel Managment Module""",
    'author': 'Arenti',
    'category': 'Category',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'views/hotel_list.xml',
        'views/manager_list.xml',
        'views/employee_list.xml'
    ],
    'sequence': -2,
    'installable': True,
    'auto_install': False,
    'application': True,
}
