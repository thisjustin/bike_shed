from django.test import TestCase
from django.contrib.auth.models import User

from decimal import Decimal
from apps.bikes.models import Brand, Bike


class BikeTestCase(TestCase):
    def setUp(self) -> None:
        user, status = User.objects.get_or_create(username='username', password='password')
        brand = Brand.objects.create(name='brand_name')
        Bike.objects.create(brand=brand, type='type', model='model', headline='headline', description='description',
                            size=1, price=2, created_by=user)

    def tearDown(self) -> None:
        brand = Brand.objects.get(id=1)
        bike = Bike.objects.get(id=1)
        brand.delete()
        bike.delete()

    def test_brand_instance(self):
        brand = Brand.objects.get(id=1)
        self.assertEqual(brand.name, 'brand_name')
        self.assertIsInstance(brand.bike.latest('created_date'), Bike)

    def test_bike_instance(self):
        bike = Bike.objects.get(id=1)
        self.assertEqual(bike.brand.id, 1)
        self.assertEqual(bike.type, 'type')
        self.assertEqual(type(bike.model), str)
        self.assertEqual(bike.size, 1)
        self.assertEqual(type(bike.price), Decimal)
        self.assertIsInstance(bike.created_by, User)
