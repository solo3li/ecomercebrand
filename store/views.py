from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Min, Max
from .models import Category, Product, ProductVariant, Cart, CartItem, Order, OrderItem

def home(request):
    featured = Product.objects.all()[:4]
    return render(request, 'store/index.html', {'featured': featured})

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    # Get all available sizes and colors from variants
    available_sizes = ProductVariant.objects.values_list('size', flat=True).distinct()
    available_colors = ProductVariant.objects.values_list('color', flat=True).distinct()

    # Filtering Logic
    cat_id = request.GET.get('category')
    size = request.GET.get('size')
    color = request.GET.get('color')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if cat_id:
        products = products.filter(category_id=cat_id)
    
    if size:
        products = products.filter(variants__size=size).distinct()
        
    if color:
        products = products.filter(variants__color=color).distinct()
        
    if min_price:
        products = products.filter(price__gte=min_price)
        
    if max_price:
        products = products.filter(price__lte=max_price)

    context = {
        'products': products,
        'categories': categories,
        'available_sizes': available_sizes,
        'available_colors': available_colors,
    }
    return render(request, 'store/shop.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    variants = product.variants.all()
    
    # Extract unique sizes and colors for this product
    sizes = list(set([v.size for v in variants]))
    colors = list(set([v.color for v in variants]))
    
    context = {
        'product': product,
        'sizes': sizes,
        'colors': colors,
        'variants': variants,
    }
    return render(request, 'store/product_detail.html', context)

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    return render(request, 'store/contact.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'store/auth/register.html', {'form': form})

def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_id=session_id, user=None)
    return cart

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    size = request.POST.get('size')
    color = request.POST.get('color')
    
    cart = get_or_create_cart(request)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product, size=size, color=color
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        
    return redirect('cart')

def view_cart(request):
    cart = get_or_create_cart(request)
    return render(request, 'store/cart.html', {'cart': cart})

@login_required
def checkout(request):
    cart = get_or_create_cart(request)
    if cart.items.count() == 0:
        return redirect('shop')
        
    if request.method == 'POST':
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        
        total_price = sum(item.product.price * item.quantity for item in cart.items.all())
        
        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            address=address,
            city=city,
            postal_code=postal_code,
            status='placed'
        )
        
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                size=item.size,
                color=item.color,
                quantity=item.quantity,
                price=item.product.price
            )
            
        cart.items.all().delete()
        return redirect('order_tracking', pk=order.pk)
        
    return render(request, 'store/checkout.html', {'cart': cart})

@login_required
def order_tracking(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'store/order_tracking.html', {'order': order})

@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/auth/profile.html', {'orders': orders})
