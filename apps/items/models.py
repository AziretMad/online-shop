from django.db import models


class ParentCategory(models.Model):
    name = models.CharField('Наименование', max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Главная категория'
        verbose_name_plural = 'Главные категории'


class Category(models.Model):
    name = models.CharField('Наименование', max_length=50)
    slug = models.SlugField(max_length=50)
    parent_categories = models.ManyToManyField(
        ParentCategory, verbose_name='Главные категории'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')
    categories = models.ManyToManyField(
        Category, verbose_name='Категории'
    )
    quantity = models.IntegerField("Количество")
    price = models.DecimalField("Цена", max_digits=5, decimal_places=2)
    image = models.ImageField("Картинка", upload_to="items")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
