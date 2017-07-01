from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class worker(models.Model):

    class Meta():
        db_table='worker'
        verbose_name='Сотрудник'
        verbose_name_plural='Сотрудники'

    DEPARTMENT=(('бухгалтерия','Бухгалтерия'),
                ('отдел механизации','Отдел механизации'))

    name = models.CharField(max_length=200, verbose_name="ФИО Сотрудника")
    image = models.ImageField(null=True, upload_to='image/worker/%Y/%m/%d/', blank=True,
                              verbose_name="Фото сотрудника")

    phone = models.CharField(max_length= 30, verbose_name="Номер телефона", blank=True)
    department = models.CharField(max_length=50, choices=DEPARTMENT, verbose_name="Выберите отдел")
    info = models.TextField(blank=True,verbose_name="Информация")

    def __str__(self):
        return self.name

class machine(models.Model):

    class Meta():
        db_table = 'machine'
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'


    name = models.CharField(max_length=200, verbose_name="Название технического средства", unique=True)
    image = models.ImageField(null=True, upload_to='image/machine/%Y/%m/%d/', blank=True,
                              verbose_name="Фото сотрудника")
    text = models.TextField(blank=True, verbose_name="Описание технического средства")

    def __str__(self):
        return self.name

class prise(models.Model):

    CATEGORY = (
        ('продукция','Продукция'),('услуги','Услуги')
    )

    class Meta():
        db_table = 'prise'
        verbose_name = 'Прайслист'
        verbose_name_plural = 'Прайслист'

    category = models.CharField(max_length=200, choices=CATEGORY, blank=True,verbose_name="Категория",)
    name = models.CharField(max_length=200, unique=True, verbose_name="Назнавие")
    text = models.TextField(verbose_name="Описание", blank=True)
    prise_item = models.CharField(max_length=20,blank=False,verbose_name="Цена")
    size = models.CharField(max_length=200, verbose_name="Единица измерения")

    def __str__(self):
        return self.name
