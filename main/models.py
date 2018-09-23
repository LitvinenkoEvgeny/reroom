import os
from django.db import models
from django.utils.html import mark_safe
from django.core.exceptions import ValidationError


# FIXME: refactor this shit
class IndexPage(models.Model):
    UPLOAD_TO = os.path.join('admin', 'index')

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

    learn_more_text = models.CharField(max_length=1000, verbose_name='Текст для кнопки узнать больше')
    contact_info = models.CharField(max_length=17, verbose_name='Номер телефона')
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
