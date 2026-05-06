import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bervado_project.settings')
django.setup()

from store.models import Category, Product, ProductVariant

data = [
    {
        'category': 'Shirts',
        'products': [
            {
                'name': 'The Milano Linen Shirt',
                'description': 'A lightweight, breathable linen shirt perfect for summer on the Riviera.',
                'price': '85.00',
                'colors': ['Navy', 'Cream', 'Olive'],
                'sizes': ['S', 'M', 'L', 'XL']
            },
            {
                'name': 'Classic Oxford Button-Down',
                'description': 'A timeless Oxford shirt tailored for a smart-casual silhouette.',
                'price': '95.00',
                'colors': ['White', 'Light Blue'],
                'sizes': ['S', 'M', 'L', 'XL']
            }
        ]
    },
    {
        'category': 'Knitwear',
        'products': [
            {
                'name': 'Classic Cashmere Quarter-Zip',
                'description': 'Knitted from 100% pure cashmere for incredibly soft, lightweight warmth.',
                'price': '145.00',
                'colors': ['Navy', 'Charcoal', 'Cream'],
                'sizes': ['M', 'L', 'XL']
            }
        ]
    },
    {
        'category': 'Trousers',
        'products': [
            {
                'name': 'Tailored Chino Trousers',
                'description': 'Classic flat-front chinos made from stretch-cotton twill.',
                'price': '110.00',
                'colors': ['Navy', 'Olive', 'Khaki'],
                'sizes': ['30', '32', '34', '36']
            }
        ]
    }
]

def run():
    print("Populating database with categories and variants...")
    
    if Product.objects.exists():
        print("Products already exist. Skipping population.")
        return
    
    for cat_data in data:
        category, _ = Category.objects.get_or_create(name=cat_data['category'])
        
        for prod_data in cat_data['products']:
            product = Product.objects.create(
                category=category,
                name=prod_data['name'],
                description=prod_data['description'],
                price=prod_data['price']
            )
            
            for color in prod_data['colors']:
                for size in prod_data['sizes']:
                    ProductVariant.objects.create(
                        product=product,
                        size=size,
                        color=color,
                        stock=15
                    )
            print(f"Created {product.name} with {len(prod_data['colors']) * len(prod_data['sizes'])} variants.")

if __name__ == '__main__':
    run()
