import os
import random
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class SingleInstansOnlyMixin(object):
    def save(self, *args, **kwargs):
        if self.__class__.objects.exists() and not self.pk:
            raise ValidationError(
                f'Вы не можете дважды добавить объект {self._meta.verbose_name}, просто редактируйте предыдущий')
        return super(SingleInstansOnlyMixin, self).save(*args, **kwargs)


# FIXME: refactor this shit
class IndexPage(SingleInstansOnlyMixin, models.Model):
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


class ContactsPage(SingleInstansOnlyMixin, models.Model):
    title = models.CharField(max_length=50, verbose_name='title страницы')
    heading = models.TextField(verbose_name='Заголовок на первом экране')
    company_name_heading = models.TextField(verbose_name='Заголовок названия компании')
    addr_heading = models.TextField(verbose_name='Заголовок адреса')
    phone_heading = models.TextField(verbose_name='Заголовок телефона')
    working_time_heading = models.TextField(verbose_name='Заголовок время работы')
    email_heading = models.TextField(verbose_name='Заголовок email')
    form_heading = models.TextField(verbose_name='Заголовок над формой')
    submit_text = models.TextField(verbose_name='Текст в кнопке формы')

    class Meta:
        verbose_name = 'Страница контакты'
        verbose_name_plural = 'Страница контакты'

    def __str__(self):
        return 'Страница Контакты'


class ContactInfo(SingleInstansOnlyMixin, models.Model):
    company_name = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    addr = models.CharField(max_length=500)
    working_time = models.CharField(max_length=500)
    instagram_text = models.CharField(max_length=500)
    instagram_link = models.URLField(max_length=500)
    development = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return 'Контакты'


class ProjectsPage(SingleInstansOnlyMixin, models.Model):
    services_page_title = models.CharField(max_length=200)

    single_item_top_left_heading = models.CharField(max_length=500)
    single_item_top_right_heading = models.CharField(max_length=500)
    single_item_bottom_left_heading = models.CharField(max_length=500)
    single_item_bottom_right_heading = models.CharField(max_length=500)

    def get_random_catalog_items(self, number_of_items):
        return random.sample(list(self.catalogitem_set.filter(show_on_main=True)), number_of_items)


class CatalogItem(models.Model):
    UPLOAD_TO = os.path.join('admin', 'services')

    SERVICE_TYPES = (
        ('design', 'Дизайн'),
        ('house', 'Ремонт квартир и домов'),
        ('office', 'Ремонт офисов'),
        ('construction', 'Строительство домов'),
    )

    service = models.ForeignKey('ProjectsPage', on_delete=models.CASCADE, blank=True)
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


class ServicesPage(models.Model):
    title = models.CharField(max_length=500)
    heading = models.TextField(max_length=500)
    text_block_left = models.TextField(max_length=1500)
    text_block_right = models.TextField(max_length=1500)


class ServicesItem(models.Model):
    SERVICE_TYPE = [
        ['design', 'Дизайн'],
        ['house repair', 'Ремонт квартир и домов'],
        ['office repair', 'Ремонт офисов'],
        ['construction', 'Строительство домов'],
    ]

    UPLOAD_TO = os.path.join('admin', 'index', 'services')

    type = models.CharField(max_length=150, choices=SERVICE_TYPE)
    name = models.TextField(max_length=500)
    preview_img = models.ImageField(upload_to=UPLOAD_TO, blank=True)
    main_img = models.ImageField(upload_to=UPLOAD_TO, blank=True)
    image_text = models.TextField(max_length=500)
    projects = models.ManyToManyField('CatalogItem', blank=True)
    headings_with_text_blocks = models.ManyToManyField('HeadingAndText', blank=True)
    accordion = models.ForeignKey('ServiceItemAccordion', blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:services-item', kwargs={'type': self.type})

    # Можно создать только один инстанс с типом Дизайн/Ремонт квартир/Ремонт офисов etc.
    def save(self, *args, **kwargs):
        first_service_item = ServicesItem.objects.filter(type=self.type).first()
        if self.pk == first_service_item.pk:
            return super(ServicesItem, self).save(*args, **kwargs)
        else:
            raise ValidationError(f'Вы можете создать только один объект с типом {self.type}')


class ServiceItemAccordion(models.Model):
    title = models.TextField(max_length=100)
    items = GenericRelation('HeadingAndText')

    def __str__(self):
        return self.title


class HeadingAndText(models.Model):
    heading = models.TextField(max_length=300)
    text = models.TextField(max_length=5000)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.heading


class HeadingAndTextImage(models.Model):
    UPLOAD_TO = os.path.join('admin', 'misc')

    heading = models.ForeignKey('HeadingAndText', on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to=UPLOAD_TO)
