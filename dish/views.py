from django.shortcuts import render
from django.utils import timezone
#from mirsaonews.models import News
#from articles.models import Article
#from .models import About
# Create your views here.


def index(request) :
    # news = news = Article.objects.filter(
    #         **{'type_item': "news", 'status': "public", 'published_date__lte':timezone.now(),}).order_by('-published_date')[:6]
    # articles = None;#Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:6]
    return render(request, 'home/index.html')

# def about(request):
#     about_model = None #About.objects.all().order_by('-id').first()
#     if not about_model :
#         return render(request,'about.html', {'about_model': None})
#     return render(request,'about.html', {'about_model':about_model})
#

