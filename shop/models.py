from django.db import models
from django.utils import timezone
from django.urls import reverse
# from tinymce.models import HTMLField
# from filebrowser.fields import FileBrowseField
from caffemain.apps import transliterate
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200,
                              db_index=True),
    )
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True, default='')
    class Meta:
        # ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        self.create_slug()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def create_slug(self):
        if self.slug == "":
            self.slug = transliterate(self.name)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200, db_index=True),
        description=models.TextField(blank=True)
    )
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)

    slug = models.SlugField(verbose_name='Slug', unique=True, db_index=True, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # main_image = models.FilePathField(verbose_name='Main image for shop')
    dish_weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Weight of shop')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'

    # this is not needed for create link
    def save(self, *args, **kwargs):
        self.create_slug()
        super(Product, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        if self.slug == "":
            self.slug = transliterate(self.name)
        self.save()

    def create_slug(self):
        if self.slug == "":
            self.slug = transliterate(self.name)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])


# class DishTranslate(models.Model):
#     dish_main = models.ForeignKey(Product, on_delete=models.CASCADE)
#     lang_code = models.CharField(verbose_name="Language Code", max_length=5)
#     title = models.CharField(max_length=55, verbose_name='Title')
#     short_body = models.TextField(verbose_name='Short annotation', null=True, blank=True)
#     body = models.TextField(verbose_name='Full text')
#     dish_type = models.ForeignKey(DishType, on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         verbose_name = 'DishTranslate'
#         verbose_name_plural = 'DishTranslates'
#
#         # this is not needed for create link
#
#     def save(self, *args, **kwargs):
#         super(DishTranslate, self).save(*args, **kwargs)
#

class DishGallery(models.Model):
    dish_main = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=55, verbose_name='Title')
    file_path = models.FilePathField(verbose_name='File path')
