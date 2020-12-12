from django.db import models
from django.utils import timezone
# from tinymce.models import HTMLField
# from filebrowser.fields import FileBrowseField
from caffemain.apps import transliterate


class Dish(models.Model):
     slug = models.SlugField(verbose_name='Slug', unique=True, blank=True)
     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
     #main_image = models.FilePathField(verbose_name='Main image for dish')
     dish_weight = models.SmallIntegerField(verbose_name='Weight of dish')
     dish_type = models.CharField(verbose_name='Type of dish')
     created_date = models.DateTimeField(
         default=timezone.now)
     published_date = models.DateTimeField(
         blank=True, null=True)
     dish_price = models.FloatField(verbose_name='Price')

     class Meta:
         verbose_name = 'Dish'
         verbose_name_plural = 'Dishes'

     # this is not needed for create link
     def save(self, *args, **kwargs):
         self.createSlug()
         super(Dish, self).save(*args, **kwargs)

    def publish(self):
        """

        :type self: object
        """
        self.published_date = timezone.now()
        if (self.slug == ""):
            self.slug = transliterate(self.title)
        self.save()

    def createSlug(self):
        if (self.slug == ""):
            self.slug = transliterate(self.title)

    def __str__(self):
        return self.title

class DishTranslate(models.Model):
    lang_code = models.CharField(verbose_name="Language Code", max_length=5)
    title = models.CharField(max_length=55, verbose_name='Title')
    short_body = models.TextField(verbose_name='Short annotation', null=True, blank=True)
    body = models.TextField(verbose_name='Full text')
