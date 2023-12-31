from odoo import http
from odoo.http import request

from . import base_controllers as res

class SupplierAPI(http.Controller):
    
  @http.route('/api/supplier', auth='user', methods=['GET'])
  def get_suppliers(self, **kw):
    if not request.env.user.can_use_api:
      return res.mapper("Not Authorized for this feature", status=401)

    suppliers = request.env['custom_material.supplier'].search([])
    data = suppliers.read(['name', 'address', 'phone'])
    return res.mapper("Supplier List", data=data, status=200)
  
  @http.route('/api/supplier/<int:id>', auth='user', methods=['GET'])
  def get_material(self, id, **kw):
    if not request.env.user.can_use_api:
      return res.mapper("Not Authorized for this feature", status=401)

    supplier = request.env['custom_material.supplier'].browse(id)
    if not supplier.exists():
      return res.mapper("Data not found", status=422)

    data = supplier.read(['name', 'address', 'phone'])[0]
    return res.mapper("Supplier Detail", data=data, status=200)

  @http.route('/api/supplier', type='json', auth='user', methods=['POST'])
  def create_supplier(self, **kw):
    if not request.env.user.can_use_api:
      return res.mapper("Not Authorized for this feature", status=401)
    
    params = request.jsonrequest
    try:
      supplier = request.env['custom_material.supplier'].create({
        'name': params.get('name'),
        'address': params.get('address'),
        'phone': params.get('phone'),
      })

      data = {
        'id': supplier.id,
        'name': supplier.name,
        'address': supplier.address,
        'phone': supplier.phone,
      }

      return res.mapper("Supplier Create", data=data, status=201, object_only=True)
    except Exception as e:
      return res.mapper(str(e), status=422, object_only=True)

  @http.route('/api/supplier/<int:id>', type='json', auth='user', methods=['PUT'])
  def update_supplier(self, id, **kw):
    if not request.env.user.can_use_api:
      return res.mapper("Not Authorized for this feature", status=401)
    
    params = request.jsonrequest
    try:
      supplier = request.env['custom_material.supplier'].browse(id)
      if not supplier:
        return res.mapper("Supplier not found", status=404, object_only=True)

      supplier.write({
        'name': params.get('name', supplier.name),
        'address': params.get('address', supplier.address),
        'phone': params.get('phone', supplier.phone),
      })

      data = {
        'id': supplier.id,
        'name': supplier.name,
        'address': supplier.address,
        'phone': supplier.phone,
      }

      return res.mapper("Supplier Updated", data=data, status=200, object_only=True)
    except Exception as e:
      return res.mapper(str(e), status=422, object_only=True)

  @http.route('/api/supplier/<int:id>', auth='user', methods=['DELETE'], csrf=False)
  def delete_supplier(self, id):
    if not request.env.user.can_use_api:
      return res.mapper("Not Authorized for this feature", status=401)
    try:
      supplier = request.env['custom_material.supplier'].browse(id)
      if not supplier:
        return res.mapper("Supplier not found", status=404, object_only=True)

      supplier.unlink()
      return res.mapper("Supplier Destroyed", status=200)
    except Exception as e:
      return res.mapper(str(e), status=422)