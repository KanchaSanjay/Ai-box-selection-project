import os
import sys
from pathlib import Path

# Ensure project root is on sys.path so Django can import the `config` package
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

os.environ['USE_SQLITE'] = '1'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from shipping.models import Product, Box
from decimal import Decimal

# Create product if not exists
p, created = Product.objects.get_or_create(
    name='Book',
    defaults={'length': 10.0, 'width': 10.0, 'height': 5.0, 'weight': 1.0}
)
print('Product:', p.id, p.name, 'created' if created else 'exists')

# Create box if not exists
b, created = Box.objects.get_or_create(
    name='Small Box',
    defaults={'length': 20.0, 'width': 20.0, 'height': 10.0, 'max_weight': 5.0, 'cost': Decimal('50.00')}
)
print('Box:', b.id, b.name, 'created' if created else 'exists')
