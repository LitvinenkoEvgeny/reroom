from django.db import models


# Create your models here.

class IndexPage(models.Model):
    learn_more_text = models.CharField(max_length=1000, verbose_name='Текст для кнопки узнать больше')
    contact_info = models.CharField(max_length=17, verbose_name='Номер телефона')
    first_heading = models.CharField(max_length=1000, verbose_name='Заголовок на главной странице')
    down_text = models.CharField(max_length=100, verbose_name='Текст "Вниз"')
    second_screen_heading = models.CharField(max_length=1000, verbose_name='Заголовок второго экрана')
    second_screen_descr = models.CharField(max_length=1000, verbose_name='Описание второго экрана')
    third_screen_heading = models.CharField(max_length=1000, verbose_name='Заголовок третьего экрана')
    third_screen_descr = models.CharField(max_length=1000, verbose_name='Описание третьего экрана')
    fourth_screen_heading = models.CharField(max_length=1000, verbose_name='Заголовок четвертого экрана')
    fourth_screen_descr = models.CharField(max_length=1000, verbose_name='Описание четвертого экрана')
    fifth_screen_heading = models.CharField(max_length=1000, verbose_name='Заголовок пятого экрана')
    fifth_screen_descr = models.CharField(max_length=1000, verbose_name='Описание пятого экрана')
    sixth_screen_heading = models.CharField(max_length=1000, verbose_name='Заголовок шестого экрана')
    seventh_screen_form_heading = models.CharField(max_length=1000, verbose_name='Заголовок формы')
    seventh_screen_form_button_text = models.CharField(max_length=1000, verbose_name='Текст в кнопке отправить')
