{
  'name': "Material",
  'summary': "Manage your stock and logistics activities for material",
  'description': """
    This module is used to manage your stock and logistics activities for material. Keep track of your stock levels, serial numbers, etc.
  """,
  'author': "Akise7",
  'website': "https://siap.tech",
  'category': 'Inventory/Inventory',
  'version': '0.1',

  'depends': ['base'],

  'data': [
    'security/ir.model.access.csv',
    'views/material_views.xml',
    'views/supplier_views.xml',
    'views/material_type_views.xml',
    'views/material_type_seed.xml',
    'views/res_user_view.xml'
  ],
  'installable': True,
  'application': True,
}
