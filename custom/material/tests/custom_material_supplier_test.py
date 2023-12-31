from odoo.tests.common import TransactionCase

class TestCustomMaterialSupplier(TransactionCase):

  def setUp(self):
    super(TestCustomMaterialSupplier, self).setUp()

    self.CustomMaterialSupplier = self.env['custom_material.supplier']

  def test_01_check_supplier(self):
    """
    Check the creation of a supplier
    """
    supplier = self.CustomMaterialSupplier.create({
      'name': 'Test Supplier',
      'address': 'Test Address',
      'phone': '1234567890',
    })

    self.assertEqual(supplier.name, 'Test Supplier')
    self.assertEqual(supplier.address, 'Test Address')
    self.assertEqual(supplier.phone, '1234567890')

  def test_02_check_unique_phone(self):
    """
    Check the phone uniqueness constraint
    """
    self.CustomMaterialSupplier.create({
      'name': 'Test Supplier 1',
      'address': 'Test Address 1',
      'phone': '1234567890',
    })

    with self.assertRaises(Exception):
      self.CustomMaterialSupplier.create({
        'name': 'Test Supplier 2',
        'address': 'Test Address 2',
        'phone': '1234567890',
      })