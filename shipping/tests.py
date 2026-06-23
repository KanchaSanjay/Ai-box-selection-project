from django.test import TestCase
from .models import Product, Box
from .services import recommend_box


class RecommendBoxTests(TestCase):
    def setUp(self):
        # create some boxes
        Box.objects.create(name='Small Box', length=10, width=10, height=5, max_weight=2, cost='5.00')
        Box.objects.create(name='Medium Box', length=50, width=40, height=40, max_weight=20, cost='15.00')
        Box.objects.create(name='Large Box', length=100, width=100, height=100, max_weight=100, cost='50.00')

        # products
        self.p1 = Product.objects.create(name='A', length=10, width=8, height=2, weight=1)
        self.p2 = Product.objects.create(name='B', length=20, width=10, height=3, weight=2)

    def test_recommend_box_basic(self):
        box = recommend_box([self.p1, self.p2])
        self.assertIsNotNone(box)
        self.assertEqual(box.name, 'Medium Box')

    def test_no_products(self):
        box = recommend_box([])
        self.assertIsNone(box)
