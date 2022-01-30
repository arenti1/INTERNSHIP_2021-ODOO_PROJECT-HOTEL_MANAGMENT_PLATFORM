# -*- coding: utf-8 -*-
{
    'name': "Bookings",
    'summary': """
        Manage everything related to your reservations""",
    'description': """
        Manage everything related to reservations""",
    'author': "Arenti",
    'website': "http://www.yourcompany.com",
    'category': 'Category',
    'version': '0.1',
    'depends': ['Hotel', 'base'],
    'data': [

        'views/bookings_view.xml',
        'views/clients_view.xml',
        'reports/report.xml',
        'reports/report_layout.xml',
        'views/cron.xml',
        'views/invoice_test_view.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'sequence': -1,
    'installable': True,
    'auto_install': False,
    'application': True,
}