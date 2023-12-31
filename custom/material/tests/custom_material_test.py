from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestCustomMaterial(TransactionCase):
  def setUp(self):
    super(TestCustomMaterial, self).setUp()

    self.CustomMaterial = self.env['custom_material.material']
    self.MaterialType = self.env['custom_material.material_type'].create({
      'name': 'Test Type',
      'code': 'TT',
    })
    self.Supplier = self.env['custom_material.supplier'].create({
      'name': 'Test Supplier',
      'address': 'Test Address',
      'phone': '1234567890',
    })

  def test_01_check_material_creation(self):
    """
    Check the creation of a material
    """
    material = self.CustomMaterial.create({
      'name': 'Test Material',
      'code': 'TM',
      'material_type_id': self.MaterialType.id,
      'supplier_id': self.Supplier.id,
      'description': 'Test Description',
      'buy_price': 50.0,
    })

    self.assertEqual(material.name, 'Test Material')
    self.assertEqual(material.code, 'TM')
    self.assertEqual(material.description, 'Test Description')
    self.assertEqual(material.buy_price, 50.0)

  def test_02_check_buy_price_constraint(self):
    """
    Check the buy_price constraint
    """
    with self.assertRaises(ValidationError):
        self.CustomMaterial.create({
          'name': 'Test Material 2',
          'code': 'TM2',
          'material_type_id': self.MaterialType.id,
          'supplier_id': self.Supplier.id,
          'description': 'Test Description 2',
          'buy_price': 150.0,
        })

  def test_03_check_unique_code(self):
    """
    Check the code uniqueness constraint
    """
    self.CustomMaterial.create({
      'name': 'Test Material 3',
      'code': 'TM3',
      'material_type_id': self.MaterialType.id,
      'supplier_id': self.Supplier.id,
      'description': 'Test Description 3',
      'buy_price': 50.0,
    })

    with self.assertRaises(ValidationError):
      self.CustomMaterial.create({
        'name': 'Test Material 4',
        'code': 'TM3',
        'material_type_id': self.MaterialType.id,
        'supplier_id': self.Supplier.id,
        'description': 'Test Description 4',
        'buy_price': 50.0,
      })