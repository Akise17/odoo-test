from odoo import http
from odoo.http import request

from . import base_controllers as res

class MaterialAPI(http.Controller):
    
  @http.route('/api/material', auth='user', methods=['GET'])
  def list_materials(self, **kw):
    if not request.env.user.can_use_api:
      return res.mapper("Not Authorized for this feature", status=401)
    
    try:
      material_type_name = kw.get('filters[material_type_name]')

      domain = []
      if material_type_name:
        material_type = request.env['custom_material.material_type'].search([('name', '=', material_type_name)])
        domain.append(('material_type_id', '=', material_type.id))

      materials = request.env['custom_material.material'].search(domain)
      data = []
      for material in materials:
        data.append({
          'id': material.id,
          'name': material.name,
          'code': material.code,
          'material_type_id': material.material_type_id.id,
          'supplier_id': material.supplier_id.id,
          'description': material.description,
          'buy_price': material.buy_price,
        })

      return res.mapper("Material List", data=data, status=200)
    except Exception as e:
      return res.mapper(str(e), status=422)
  
  @http.route('/api/material/<int:id>', auth='user', methods=['GET'])
  def get_material(self, id, **kw):
    if not request.env.user.can_use_api:
      return res.mapper("Not Authorized for this feature", status=401)

    material = request.env['custom_material.material'].browse(id)
    if not material.exists():
      return res.mapper("Data not found", status=422)

    data = {
      'id': material.id,
      'name': material.name,
      'code': material.code,
      'material_type_id': material.material_type_id.id,
      'supplier_id': material.supplier_id.id,
      'description': material.description,
      'buy_price': material.buy_price,
    }
    return res.mapper("material Detail", data=data, status=200)

  @http.route('/api/material', type='json', auth='user', methods=['POST'])
  def create_material(self, **kw):
    if not request.env.user.can_use_api:
      return res.mapper("Not Authorized for this feature", status=401)
    
    params = request.jsonrequest
    try:
      material = request.env['custom_material.material'].create({
        'name': params.get('name'),
        'code': params.get('code'),
        'material_type_id': params.get('material_type_id'),
        'supplier_id': params.get('supplier_id'),
        'description': params.get('description'),
        'buy_price': params.get('buy_price'),
      })

      data = {
        'id': material.id,
        'name': material.name,
        'code': material.code,
        'material_type_id': material.material_type_id.id,
        'supplier_id': material.supplier_id.id,
        'description': material.description,
        'buy_price': material.buy_price,
      }

      return res.mapper("material Create", data=data, status=201, object_only=True)
    except Exception as e:
      return res.mapper(str(e), status=422, object_only=True)

  @http.route('/api/material/<int:id>', type='json', auth='user', methods=['PUT'])
  def update_material(self, id, **kw):
    if not request.env.user.can_use_api:
      return res.mapper("Not Authorized for this feature", status=401)
    
    params = request.jsonrequest
    try:
      material = request.env['custom_material.material'].browse(id)
      if not material:
        return res.mapper("material not found", status=404, object_only=True)

      material.write({
        'name': params.get('name'),
        'code': params.get('code'),
        'material_type_id': params.get('material_type_id'),
        'supplier_id': params.get('supplier_id'),
        'description': params.get('description'),
        'buy_price': params.get('buy_price'),
      })

      data = {
        'id': material.id,
        'name': material.name,
        'code': material.code,
        'material_type_id': material.material_type_id.id,
        'supplier_id': material.supplier_id.id,
        'description': material.description,
        'buy_price': material.buy_price,
      }

      return res.mapper("material Updated", data=data, status=200, object_only=True)
    except Exception as e:
      return res.mapper(str(e), status=422, object_only=True)

  @http.route('/api/material/<int:id>', auth='user', methods=['DELETE'], csrf=False)
  def delete_material(self, id):
    if not request.env.user.can_use_api:
      return res.mapper("Not Authorized for this feature", status=401)
    try:
      material = request.env['custom_material.material'].browse(id)
      if not material:
        return res.mapper("material not found", status=404, object_only=True)

      material.unlink()
      return res.mapper("material Destroyed", status=200)
    except Exception as e:
      return res.mapper(str(e), status=422)