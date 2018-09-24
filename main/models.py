import os
import random
from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.core.exceptions import ValidationError


# FIXME: refactor this shit
class IndexPage(models.Model):
    UPLOAD_TO = os.path.join('admin', 'index')

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

    learn_more_text = models.CharField(max_length=1000, verbose_name='Текст для кнопки узнать больше')
    first_heading = models.CharField(max_length=1000, verbose_name='Заголовок на главной странице')
    first_image = models.ImageField(verbose_name='Картинка, отображающаяся на главной странице', blank=True,
                                    upload_to=UPLOAD_TO)
    down_text = models.CharField(max_length=100, verbose_name='Текст "Вниз"')
    second_screen_heading = models.TextField(max_length=1000, verbose_name='Заголовок второго экрана')
    second_screen_image = models.ImageField(verbose_name='Картинка второго экрана', blank=True)
    second_screen_descr = models.TextField(max_length=1000, verbose_name='Описание второго экрана')
    third_screen_heading = models.TextField(max_length=1000, verbose_name='Заголовок третьего экрана')
    third_screen_image = models.ImageField(verbose_name='Картинка третьего экрана', blank=True, upload_to=UPLOAD_TO)
    third_screen_descr = models.TextField(max_length=1000, verbose_name='Описание третьего экрана')
    fourth_screen_heading = models.TextField(max_length=1000, verbose_name='Заголовок четвертого экрана')
    fourth_screen_image = models.ImageField(verbose_name='Картинка четвертого экрана', blank=True, upload_to=UPLOAD_TO)
    fourth_screen_descr = models.TextField(max_length=1000, verbose_name='Описание четвертого экрана')
    fifth_screen_heading = models.TextField(max_length=1000, verbose_name='Заголовок пятого экрана')
    fifth_screen_image = models.ImageField(verbose_name='Картинка пятого экрана', blank=True, upload_to=UPLOAD_TO)
    fifth_screen_descr = models.TextField(max_length=1000, verbose_name='Описание пятого экрана')
    sixth_screen_heading = models.TextField(max_length=1000, verbose_name='Заголовок шестого экрана')
    seventh_screen_form_heading = models.CharField(max_length=1000, verbose_name='Заголовок формы')
    seventh_screen_form_button_text = models.CharField(max_length=1000, verbose_name='Текст в кнопке отправить')

    def __str__(self):
        return 'Главная страница'

    def save(self, *args, **kwargs):
        if IndexPage.objects.exists() and not self.pk:
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'Вы не можете дважды добавить объект главной страницы, просто редактируйте предыдущий')
        return super(IndexPage, self).save(*args, **kwargs)


class ContactInfo(models.Model):
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    addr = models.CharField(max_length=500)
    instagram_text = models.CharField(max_length=500)
    instagram_link = models.URLField(max_length=500)
    development = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return 'Контакты'

    def save(self, *args, **kwargs):
        if ContactInfo.objects.exists() and not self.pk:
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'Вы не можете дважды добавить объект контакты, просто редактируйте предыдущий')
        return super(ContactInfo, self).save(*args, **kwargs)


class ServicesPage(models.Model):
    services_page_title = models.CharField(max_length=200)

    single_item_top_left_heading = models.CharField(max_length=500)
    single_item_top_right_heading = models.CharField(max_length=500)
    single_item_bottom_left_heading = models.CharField(max_length=500)
    single_item_bottom_right_heading = models.CharField(max_length=500)

    def get_random_catalog_items(self, number_of_items):
        return random.sample(list(self.catalogitem_set.filter(show_on_main=True)), number_of_items)

    def save(self, *args, **kwargs):
        if ServicesPage.objects.exists() and not self.pk:
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'Вы не можете дважды добавить объект главной страницы, просто редактируйте предыдущий')
        return super(ServicesPage, self).save(*args, **kwargs)


class CatalogItem(models.Model):
    UPLOAD_TO = os.path.join('admin', 'services')

    SERVICE_TYPES = (
        ('design', 'Дизайн'),
        ('house', 'Ремонт квартир и домов'),
        ('office', 'Ремонт офисов'),
        ('construction', 'Строительство домов'),
    )

    service = models.ForeignKey('ServicesPage', on_delete=models.CASCADE, blank=True)
    show_on_main = models.BooleanField(default=False)
    name = models.CharField(max_length=500)
    type = models.CharField(max_length=80, choices=SERVICE_TYPES)
    main_img = models.ImageField(upload_to=UPLOAD_TO, blank=True)
    top_left = models.CharField(max_length=500)
    top_right = models.CharField(max_length=500)
    bottom_left = models.CharField(max_length=500)
    bottom_right = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('main:catalog-item', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name} - {self.type}'


class CatalogItemImg(models.Model):
    image_field = models.ImageField(upload_to=CatalogItem.UPLOAD_TO, blank=True)
    catalog_item = models.ForeignKey('CatalogItem', on_delete=models.CASCADE, blank=False)
    timestamp = models.DateTimeField(auto_now=True)
