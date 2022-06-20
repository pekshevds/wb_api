from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Торговая марка (Бренд)'
        verbose_name_plural = 'Торговые марки (Бренды)'
        ordering = ['name']

class Parent(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['name']

class Object(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150)
    parent = models.ForeignKey(Parent, verbose_name='Свойство', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

class Collection(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150, default='', null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'
        ordering = ['name']

class Color(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150, default='', null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
        ordering = ['name']

class Consist(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150, default='', null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Состав'
        verbose_name_plural = 'Составы'
        ordering = ['name']

class Content(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150, default='', null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Комплектация'
        verbose_name_plural = 'Комплектации'
        ordering = ['name']

class Country(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150, default='', null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['name']

class Option(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150, default='', null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'
        ordering = ['name']

class Ext(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150, default='', null=True)
    option = models.ForeignKey(Option, verbose_name='Свойство', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'
        ordering = ['name']

class Kind(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150, default='', null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Полы'
        ordering = ['name']

class Season(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150, default='', null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'
        ordering = ['name']

class Si(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150, default='', null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Единица'
        verbose_name_plural = 'Единицы'
        ordering = ['name']

class Warehouse(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150, default='', null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        ordering = ['name']

class WBSize(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150, default='', null=True)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'
        ordering = ['name']

class ItemOfWBSize(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150, default='', null=True)
    wbsize = models.ForeignKey(WBSize, verbose_name='Размер', on_delete=models.CASCADE)
    size_min = models.PositiveIntegerField(verbose_name='Минимальный размер', default=0)
    size_max = models.PositiveIntegerField(verbose_name='Максимальный размер', default=0)


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Варианты размера'
        verbose_name_plural = 'Варианты размеров'
        ordering = ['name']

        
'''
class Supply(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150, default='', null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'
        ordering = ['name']

class Order(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150, default='', null=True)
    supply = models.ForeignKey(Supply, verbose_name='Размер', on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['name']        
        
'''