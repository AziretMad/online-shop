from django.db import models


class ParentCategory(models.Model):
    name = models.CharField('Наименование', max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Category(models.Model):
    name = models.CharField('Наименование', max_length=50)
    slug = models.SlugField(max_length=50)
    parent_categories = models.ManyToManyField(
        ParentCategory, verbose_name='Категории'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Item(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')
    categories = models.ManyToManyField(
        Category, verbose_name='Подкатегории'
    )
    quantity = models.IntegerField("Количество")
    price = models.DecimalField("Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
