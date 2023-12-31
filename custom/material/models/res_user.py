from odoo import models, fields

class ResUsers(models.Model):
  _inherit = 'res.users'

  can_use_api = fields.Boolean(string='Can Use API', default=False)