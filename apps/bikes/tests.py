from django.test import TestCase
from django.contrib.auth.models import User

from decimal import Decimal
from apps.bikes.models import Brand, Bike


class BikeTestCase(TestCase):
    def setUp(self) -> None:
        user, status = User.objects.get_or_create(username='username', password='password')
        brand = Brand.objects.create(name='Pinarello')
        Bike.objects.create(brand=brand, type='RD', model='R100', headline='Bike #0339', description='Bike desc',
                            size=35, price=12.00, created_by=user)

    def test_brand_instance(self):
        brand = Brand.objects.get(id=1)
        self.assertEqual(brand.name, 'Pinarello')

    def test_bike_instance(self):
        bike = Bike.objects.get(id=1)
        self.assertEqual(bike.brand.id, 1)
        self.assertEqual(bike.type, 'RD')
        self.assertEqual(type(bike.model), str)
        self.assertEqual(bike.size, 35)
        self.assertEqual(type(bike.price), Decimal)
        self.assertEqual(bike.created_by.__class__, User)
