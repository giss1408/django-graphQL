from django.test import TestCase
from .models import Product, Hotel

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            title="Test Product",
            price=100000,
            description="Test Description",
            surface_m2=75
        )

    def test_product_creation(self):
        self.assertTrue(isinstance(self.product, Product))
        self.assertEqual(self.product.__str__(), self.product.title)

    def test_product_fields(self):
        self.assertEqual(self.product.title, "Test Product")
        self.assertEqual(self.product.price, 100000)
        self.assertEqual(self.product.description, "Test Description")
        self.assertEqual(self.product.surface_m2, 75)

class HotelModelTest(TestCase):
    def setUp(self):
        self.hotel = Hotel.objects.create(
            name="Test Hotel",
            address="123 Test Street",
            price=200000,
            rooms=10
        )

    def test_hotel_creation(self):
        self.assertTrue(isinstance(self.hotel, Hotel))
        self.assertEqual(self.hotel.__str__(), self.hotel.name)

    def test_hotel_fields(self):
        self.assertEqual(self.hotel.name, "Test Hotel")
        self.assertEqual(self.hotel.address, "123 Test Street")
        self.assertEqual(self.hotel.price, 200000)
        self.assertEqual(self.hotel.rooms, 10)
