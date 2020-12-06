from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField
from .apps import transliterate


# class About(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Заголовок')
#     annonce = HTMLField(verbose_name='Анонс ()', null = True, blank = True)
#     body = HTMLField(verbose_name='Пполный текст')
#     link = models.CharField(max_length=255, verbose_name='Путь (ссылка)', unique=True, blank=True, default="about")
#     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     created_date = models.DateTimeField(
#         default=timezone.now)
#     published_date = models.DateTimeField(
#         blank=True, null=True)
#
#     class Meta:
#         verbose_name = 'Контакт'
#         verbose_name_plural = 'Контакти'
#
#     # this is not needed for create link
#     def save(self, *args, **kwargs):
#         self.createlink()
#         super(About, self).save(*args, **kwargs)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         if (self.link == ""):
#             self.link = transliterate(self.title)
#         self.save()
#
#     def createlink(self):
#         if (self.link == ""):
#             self.link = transliterate(self.title)
#
#     def __str__(self):
#         return self.title

