from django.db import models

class Navigation(models.Model):
    logo = models.ImageField(upload_to='img/', blank=False, verbose_name='Логотип')
    logo_text = models.TextField(blank = False, verbose_name='Название', max_length=100)
    menu_el_1 = models.TextField(blank=False, verbose_name='1 пункт меню', max_length=25)
    menu_el_2 = models.TextField(blank=False, verbose_name='2 пункт меню', max_length=25)
    menu_el_3 = models.TextField(blank=False, verbose_name='3 пункт меню', max_length=25)
    menu_el_4 = models.TextField(blank=False, verbose_name='4 пункт меню',max_length=25)
    menu_el_5 = models.TextField(blank=False, verbose_name='5 пункт меню', max_length=25)
    author = models.TextField(blank=False, verbose_name='Автор', max_length=50)
    class Meta:
        verbose_name = 'Навигация' 
        verbose_name_plural = 'Навигации'

class Main(models.Model):
    title = models.TextField(blank=True, verbose_name='Заголовок')
    text = models.TextField(blank=True, verbose_name='Описание профессии')
    img = models.ImageField(upload_to='img/', blank=True, verbose_name='картинка')
    class Meta:
        verbose_name = 'Главная' 
        verbose_name_plural = 'Главные'

class Demand(models.Model):
    title1 = models.TextField(blank=True, verbose_name='Заголовок')
    title2 = models.TextField(blank=True, verbose_name='Заголовок таблицы 1')
    table1 = models.TextField(blank=True, verbose_name='Таблица 1')
    title3 = models.TextField(blank=True, verbose_name='Заголовок таблицы 2')
    table2 = models.TextField(blank=True, verbose_name='Таблица 2')
    title4 = models.TextField(blank=True, verbose_name='Заголовок таблицы 3')
    table3 = models.TextField(blank=True, verbose_name='Таблица 3')
    img1 = models.ImageField(upload_to='img/', blank = True, verbose_name='1 график сравнения')
    img2 = models.ImageField(upload_to='img/', blank = True, verbose_name='2 график сравнения')
    img3 = models.ImageField(upload_to='img/', blank = True, verbose_name='3 график сравнения')
    class Meta:
        verbose_name = 'Востребованность' 
        verbose_name_plural = 'Востребованность'

class Geography(models.Model):
    title = models.TextField(blank=True, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Таблицы')
    first_title = models.CharField(max_length=50, blank=True, verbose_name='Заголовок для 1 фото')
    img1 = models.ImageField(upload_to='img/', blank=True, verbose_name='график 1')
    second_title = models.CharField(max_length=50, blank=True, verbose_name='Заголовок для 2 фото')
    img2 = models.ImageField(upload_to='img/', blank=True, verbose_name='график 2')
    class Meta:
        verbose_name = 'География' 
        verbose_name_plural = 'География'

class Skills(models.Model):
    first_title = models.CharField(max_length=50, blank=True, verbose_name='Заголовок для таблицы')
    content = models.TextField(blank=True, verbose_name='Таблица')
    img1 = models.ImageField(upload_to='img/', blank=True, verbose_name='График 1')
    img2 = models.ImageField(upload_to='img/', blank=True, verbose_name='График 2')
    class Meta:
        verbose_name = 'Навык' 
        verbose_name_plural = 'Навыки'


class lastVacancyModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    
    class Meta:
        verbose_name = 'Вакансия' 
        verbose_name_plural = 'Вакансии'
