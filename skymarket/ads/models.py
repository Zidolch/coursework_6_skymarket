from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=1000, null=False, blank=False)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    ad = models.ForeignKey('ads.Ad', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text

