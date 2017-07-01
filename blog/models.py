from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Category(models.Model):

    class Meta():
        db_table='category'
        verbose_name='Категория'
        verbose_name_plural='Категории'


    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_list_by_category', args=[self.slug])



class Post(models.Model):

    class Meta:
        db_table = 'post'
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


    category = models.ForeignKey(Category, verbose_name="Категория")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=200)
    image_small = ThumbnailerImageField(null=True, upload_to='image/posts/%Y/%m/%d/thumbnail/', blank=True, help_text='150x150px',verbose_name=" Картинка на категорию")
    image = models.ImageField(null=True, upload_to='image/posts/%Y/%m/%d/', blank=True,verbose_name="Заглавная картинка")
    text = RichTextUploadingField(verbose_name="Текст" )
    published_date = models.DateTimeField(
        blank=True, null=True, verbose_name="Публикация")

    like = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




    def get_absolute_url(self):

        return reverse('post_detail', args=[self.slug])
