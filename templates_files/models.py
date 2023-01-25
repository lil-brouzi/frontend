from django.db import models

class Navigation(models.Model):
    logo = models.ImageField(upload_to='media/', blank=False, verbose_name='Логотип')
    logo_text = models.TextField(blank = False, verbose_name='Название', max_length=100)
    first_menu = models.TextField(blank=False, verbose_name='Первый пункт меню', max_length=25)
    second_menu = models.TextField(blank=False, verbose_name='Второй пункт меню', max_length=25)
    thierd_menu = models.TextField(blank=False, verbose_name='Третий пункт меню', max_length=25)
    fourth_menu = models.TextField(blank=False, verbose_name='Четвертый пункт меню',max_length=25)
    fifth_menu = models.TextField(blank=False, verbose_name='Пятый пункт меню', max_length=25)
    author = models.TextField(blank=False, verbose_name='Автор', max_length=50)
    class Meta:
        verbose_name = 'Навигация' 
        verbose_name_plural = 'Навигации'

class Main(models.Model):
    title = models.TextField(blank=True, verbose_name='Заголовок')
    text = models.TextField(blank=True, verbose_name='Описание профессии')
    photo = models.ImageField(upload_to='media/', blank=False, verbose_name='Фото')
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
    photo1 = models.ImageField(upload_to='media/', blank = False, verbose_name='Первый график сравнения')
    photo2 = models.ImageField(upload_to='media/', blank = False, verbose_name='Второй график сравнения')
    photo3 = models.ImageField(upload_to='media/', blank = True, verbose_name='Третий график сравнения')
    class Meta:
        verbose_name = 'Востребованность' 
        verbose_name_plural = 'Востребованность'

class Geography(models.Model):
    title = models.TextField(blank=True, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Таблицы')
    first_title = models.CharField(max_length=50, blank=True, verbose_name='Заголовок для первого фото')
    photo1 = models.ImageField(upload_to='media/', blank=False, verbose_name='Первое фото')
    second_title = models.CharField(max_length=50, blank=True, verbose_name='Заголовок для второго фото')
    photo2 = models.ImageField(upload_to='media/', blank=False, verbose_name='Второй график')
    class Meta:
        verbose_name = 'География' 
        verbose_name_plural = 'География'

class Skills(models.Model):
    first_title = models.CharField(max_length=50, blank=True, verbose_name='Заголовок для таблицы')
    content = models.TextField(blank=True, verbose_name='Таблица')
    graph = models.ImageField(upload_to='media/', blank=False, verbose_name='График 1')
    graph2 = models.ImageField(upload_to='media/', blank=False, verbose_name='График 2')
    class Meta:
        verbose_name = 'Навык' 
        verbose_name_plural = 'Навыки'


class lastVacancyModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    
    class Meta:
        verbose_name = 'Вакансия' 
        verbose_name_plural = 'Вакансии'
