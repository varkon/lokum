from django.db import models
from django.utils import timezone
# from tinymce.models import HTMLField
# from filebrowser.fields import FileBrowseField
from .apps import transliterate


class About(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='Путь (ссылка)', unique=True, blank=True, default="about")
    phone = models.CharField(verbose_name='Phone', max_length=12)
    email = models.CharField(verbose_name='E-mail', max_length=55)
    location_text = models.CharField(verbose_name='Address', max_length=128)
    location_google = models.TextField(verbose_name='Google iframe', max_length=512)
    location_yandex = models.TextField(verbose_name='Yandex location', blank=True, null=True,max_length=512)
    location_coord = models.CharField(verbose_name='Geo coordinate', blank=True, null=True, max_length=55)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакти'

    # this is not needed for create link
    def save(self, *args, **kwargs):
        self.create_slug()
        super(About, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        if self.slug == "":
            self.slug = transliterate(self.title)
        self.save()

    def create_slug(self):
        if self.slug == "":
            self.slug = transliterate(self.title)

    def __str__(self):
        return self.title


class AboutTranslate(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    short_body = models.TextField(verbose_name='Short description', blank=True, null=True)
    body = models.TextField(verbose_name='Full description')
    lang_code = models.CharField(verbose_name='Language code', max_length=5)
    create_date = models.DateTimeField(
        default=timezone.now)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class SocialMedia(models.Model):
    title = models.CharField(verbose_name='Name of social network', unique=True, max_length=55)
    uri = models.URLField(verbose_name='address')
    show_name = models.CharField(verbose_name='Show Name', blank=True, null=True, max_length=55)
    create_date = models.DateTimeField(
        default=timezone.now)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class MediaLibrary(models.Model):
    image_path = models.FilePathField(verbose_name='File path')
    slug = models.CharField(max_length=255, verbose_name='Slag for media', unique=True, blank=True, default="about")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)
    hide = models.BooleanField(verbose_name='Is hide', blank=True, default=False)

    class Meta:
        verbose_name = 'Media Item'
        verbose_name_plural = 'Media'

    def save(self, *args, **kwargs):
        self.createSlug()
        super(MediaLibrary, self).save(*args, **kwargs)

    def createSlug(self):
        if self.slug == "":
            self.slug = transliterate(self.title)

    def __str__(self):
        return self.slug

class HeaderMenuItem(models.Model):
    position = models.SmallIntegerField(verbose_name='Position')
    href = models.URLField(verbose_name='Link')