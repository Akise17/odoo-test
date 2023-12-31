from odoo.tests.common import TransactionCase

class TestCustomMaterialType(TransactionCase):
  def setUp(self):
    super(TestCustomMaterialType, self).setUp()
    self.CustomMaterialType = self.env['custom_material.type']

  def test_01_check_type_creation(self):
    """
    Check the creation of a material type
    """
    material_type = self.CustomMaterialType.create({
      'name': 'Test Type',
      'code': 'TT',
      'description': 'Test Description',
    })

    self.assertEqual(material_type.name, 'Test Type')
    self.assertEqual(material_type.code, 'TT')
    self.assertEqual(material_type.description, 'Test Description')

  def test_02_check_unique_name(self):
    """
    Check the name uniqueness constraint
    """
    self.CustomMaterialType.create({
      'name': 'Test Type',
      'code': 'TT1',
      'description': 'Test Description 1',
    })

    with self.assertRaises(Exception):
      self.CustomMaterialType.create({
        'name': 'Test Type',
        'code': 'TT2',
        'description': 'Test Description 2',
      })