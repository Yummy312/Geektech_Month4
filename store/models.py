from django.db import models


class Product(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='product_images', verbose_name='Изображение')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    modified_date = models.DateField(auto_now=True, verbose_name='Последнее изменение')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(verbose_name='Оставьте отзыв')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)


