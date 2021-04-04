from django.db import models


class ParentCategory(models.Model):
    name = models.CharField('Наименование', max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Общая категория'
        verbose_name_plural = 'Общие категории'


class Category(models.Model):
    name = models.CharField('Наименование', max_length=50)
    slug = models.SlugField(max_length=50)
    parent_category = models.ForeignKey(
        ParentCategory,
        verbose_name='Общая категории',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(models.Model):
    name = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True
    )
    quantity = models.IntegerField("Количество")
    price = models.DecimalField("Цена", max_digits=5, decimal_places=2)
    image = models.ImageField("Картинка", upload_to="items")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
