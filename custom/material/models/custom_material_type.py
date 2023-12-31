from odoo import models, fields

class CustomMaterialType(models.Model):
  _name = 'custom_material.material_type'
  _description = 'Material Type Model'

  name = fields.Char(string='Name', required=True)
  code = fields.Char(string='Code', required=True)
  description = fields.Text(string='Description')

  _sql_constraints = [
    ('name_unique', 'UNIQUE(name)', 'The name must be unique!'),
    ('code_unique', 'UNIQUE(code)', 'The code must be unique!'),
  ]