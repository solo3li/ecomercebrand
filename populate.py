import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bervado_project.settings')
django.setup()

from store.models import Product, ProductSize

products_data = [
    {
        'name': 'The Milano Linen Shirt',
        'description': 'A lightweight, breathable linen shirt perfect for summer on the Riviera. Features a relaxed but tailored fit, point collar, and mother-of-pearl buttons.',
        'price': '85.00'
    },
    {
        'name': 'Classic Cashmere Quarter-Zip',
        'description': 'Knitted from 100% pure cashmere. This incredibly soft quarter-zip provides lightweight warmth and a perfectly structured silhouette for chilly evenings.',
        'price': '145.00'
    },
    {
        'name': 'Tailored Chino Trousers',
        'description': 'Classic flat-front chinos made from stretch-cotton twill. Designed for comfort without compromising on an elegant, clean line.',
        'price': '95.00'
    },
    {
        'name': 'Riviera Loafers',
        'description': 'Handcrafted suede loafers with a minimal, unlined structure for ultimate comfort. The perfect footwear for a subtle statement of luxury.',
        'price': '125.00'
    }
]

def run():
    print("Populating database...")
    if Product.objects.exists():
        print("Products already exist. Skipping.")
        return

    for item in products_data:
        p = Product.objects.create(
            name=item['name'],
            description=item['description'],
            price=item['price'],
        )
        for size in ['S', 'M', 'L', 'XL']:
            ProductSize.objects.create(product=p, size=size)
        print(f"Created {p.name}")

if __name__ == '__main__':
    run()
