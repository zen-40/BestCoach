from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill
from ckeditor.fields import RichTextField


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    data = models.CharField(max_length=200, verbose_name='Preferred date and time of the video call')


class ContactAdvanced(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    surname = models.CharField(max_length=200, verbose_name='Surname')
    email = models.EmailField(verbose_name='E-mail')
    contact = models.TextField(verbose_name='Message content')



class TermsAndConditions(models.Model):
    terms = models.TextField()
    privacy = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title_basic = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)



class Article(models.Model):
    category = models.CharField(max_length=200, verbose_name='Kategoria rankingu')
    name = models.CharField(max_length=200, verbose_name='Główny tytuł wyświetlany w podglądzie',)
    small_description = models.TextField(verbose_name='Krótki opis wyświetlany w podglądzie')
    author = models.CharField(max_length=200, verbose_name='Autor tematu')
    author_img = ProcessedImageField(upload_to='profile-pictures',
                                     verbose_name='Zdjęcie profilowe autora (preferowany rozmiar 200x200)',
                                processors=[ResizeToFill(200, 200)],
                                format='JPEG',
                                options={'quality': 100})
    title = models.CharField(max_length=500, verbose_name='Tytuł')
    basic_img = ProcessedImageField(upload_to='profile-pictures',
                                    verbose_name='Zdjęcie główne (preferowany rozmiar 923x498)',
                                processors=[ResizeToFill(923, 498)],
                                format='JPEG',
                                options={'quality': 100})
    content = RichTextField(verbose_name='Treść tematu')
    slug = models.SlugField(verbose_name="Nazwa wyświetlana w adresie url: http//domain.com/...",)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = '2A - BLOG - Pozostałe rankingi'
        verbose_name_plural = '2A - BLOG - Pozostałe rankingi'


class ArticleList(models.Model):
    for_article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Dla artykułu')
    name = models.CharField(max_length=200, verbose_name='Nazwa firmy/Instancji')
    content = models.TextField(blank=True, null=True, verbose_name='Treść/opis (minimalistyczny, przed opisem głównym)')
    image = ProcessedImageField(upload_to='profile-pictures',
                                blank=True, null=True,
                                verbose_name='Zdjęcie główne (preferowany rozmiar 923x328)',
                                processors=[ResizeToFill(928, 328)],
                                format='JPEG',
                                options={'quality': 100})
    logo = ProcessedImageField(upload_to='profile-pictures',
                                blank=True, null=True,
                                verbose_name='Logo',
                                processors=[ResizeToFit(250, 250)],
                                format='JPEG',
                                options={'quality': 100})
    description = RichTextField(blank=True, null=True, verbose_name='Pełna treść (opis główny firmy/isntancji)')

    def __str__(self):
        return '%s - %s' % (self.for_article, self.name)

    class Meta:
        verbose_name = '2B - BLOG - Przedmioty do pozostałych rankingów'
        verbose_name_plural = '2B - BLOG - Przedmioty do pozostałych rankingów'