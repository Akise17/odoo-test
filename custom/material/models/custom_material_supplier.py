from odoo import models, fields

class CustomMaterialSupplier(models.Model):
  _name = 'custom_material.supplier'
  _description = 'Supplier Model'

  name = fields.Char(string='Supplier Name', required=True)
  address = fields.Text(string='Address')
  phone = fields.Char(string='Phone')

  _sql_constraints = [
    ('name_unique', 'UNIQUE(phone)', 'The phone must be unique!'),
  ]