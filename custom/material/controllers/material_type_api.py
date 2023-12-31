from odoo import http
from odoo.http import request

from . import base_controllers as res

class MaterialTypeAPI(http.Controller):
    
  @http.route('/api/material_type', auth='user', methods=['GET'])
  def get_material_types(self, **kw):
    if not request.env.user.can_use_api:
      return res.mapper("Not Authorized for this feature", status=401)

    material_types = request.env['custom_material.material_type'].search([])
    data = material_types.read(['name', 'code', 'description'])
    return res.mapper("Material Type List", data=data, status=200)
  
  @http.route('/api/material_type/<int:id>', auth='user', methods=['GET'])
  def get_material(self, id, **kw):
    if not request.env.user.can_use_api:
      return res.mapper("Not Authorized for this feature", status=401)

    material_type = request.env['custom_material.material_type'].browse(id)
    if not material_type.exists():
      return res.mapper("Data not found", status=422)

    data = material_type.read(['name', 'code', 'description'])[0]
    return res.mapper("Material Type Detail", data=data, status=200)

  @http.route('/api/material_type', type='json', auth='user', methods=['POST'])
  def create_material_type(self, **kw):
    if not request.env.user.can_use_api:
      return res.mapper("Not Authorized for this feature", status=401)
    
    params = request.jsonrequest
    try:
      material_type = request.env['custom_material.material_type'].create({
        'name': params.get('name'),
        'code': params.get('code'),
        'description': params.get('description'),
      })

      data = {
        'id': material_type.id,
        'name': material_type.name,
        'code': material_type.code,
        'description': material_type.description,
      }

      return res.mapper("Material Type Create", data=data, status=201, object_only=True)
    except Exception as e:
      return res.mapper(str(e), status=422, object_only=True)

  @http.route('/api/material_type/<int:id>', type='json', auth='user', methods=['PUT'])
  def update_material_type(self, id, **kw):
    if not request.env.user.can_use_api:
      return res.mapper("Not Authorized for this feature", status=401)
    
    params = request.jsonrequest
    try:
      material_type = request.env['custom_material.material_type'].browse(id)
      if not material_type:
        return res.mapper("Material Type not found", status=404, object_only=True)

      material_type.write({
        'name': params.get('name', material_type.name),
        'code': params.get('code', material_type.code),
        'description': params.get('description', material_type.description),
      })

      data = {
        'id': material_type.id,
        'name': material_type.name,
        'code': material_type.code,
        'description': material_type.description,
      }

      return res.mapper("Material Type Updated", data=data, status=200, object_only=True)
    except Exception as e:
      return res.mapper(str(e), status=422, object_only=True)

  @http.route('/api/material_type/<int:id>', auth='user', methods=['DELETE'], csrf=False)
  def delete_material_type(self, id):
    if not request.env.user.can_use_api:
      return res.mapper("Not Authorized for this feature", status=401)
    try:
      material_type = request.env['custom_material.material_type'].browse(id)
      if not material_type:
        return res.mapper("Material Type not found", status=404, object_only=True)

      material_type.unlink()
      return res.mapper("Material Type Destroyed", status=200)
    except Exception as e:
      return res.mapper(str(e), status=422)