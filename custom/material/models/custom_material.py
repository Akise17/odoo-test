from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CustomMaterial(models.Model):
  _name = 'custom_material.material'
  _description = 'Material Model'

  name = fields.Char(string='Name', required=True)
  code = fields.Char(string='Code', required=True)
  material_type_id = fields.Many2one('custom_material.material_type', string='Type', required=True)
  supplier_id = fields.Many2one('custom_material.supplier', string='Supplier', required=True)
  description = fields.Text(string='Description')
  buy_price = fields.Float(string='Buy Price', required=True)

  _sql_constraints = [
    ('name_unique', 'UNIQUE(name)', 'The name must be unique!'),
    ('code_unique', 'UNIQUE(code)', 'The code must be unique!'),
  ]

  @api.constrains('buy_price')
  def _check_buy_price(self):
    for record in self:
      if record.buy_price > 100:
        raise ValidationError("Buy Price cannot be greater than 100.")