from django.shortcuts import render, get_object_or_404
from django.utils import timezone
#from mirsaonews.models import News
from shop.models import Category, Product
#from .models import About
# Create your views here.


def index(request, category_slug = None) :
    # news = news = Article.objects.filter(
    #         **{'type_item': "news", 'status': "public", 'published_date__lte':timezone.now(),}).order_by('-published_date')[:6]
    # articles = None;#Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:6]
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug and category_slug != 'menu':
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category,
                                     translations__language_code=language,
                                     slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'home/index.html', {'category': category,
                   'categories': categories,
                   'products': products,
                   })

def about(request):
    about_model = None #About.objects.all().order_by('-id').first()
    if not about_model :
        return render(request,'home/about.html', {'about_model': None})
    return render(request,'home/about.html', {'about_model':about_model})


def contact(request):
    return render(request, 'home/contact.html')


def change_language(request):
    request.path
