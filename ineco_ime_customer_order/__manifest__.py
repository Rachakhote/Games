# -*- coding: utf-8 -*-

{
    'name': "A Module",
    'version': '1.0',
    'depends': ['base', 'sale', 'mail', 'product'],
    'author': "Author Name",
    'category': 'Category',
    'description': """
    Description New module 
    Change by Games
    """,
    # data files always loaded at installation
    'data': [
        'views/sequence.xml',
        'views/customer_order_view.xml',
        'views/product_product_view.xml',
        'views/security.xml',
        'views/customer_order_report.xml',
        'views/customer_order_sticker.xml',
        'views/customer_order_label.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
}
