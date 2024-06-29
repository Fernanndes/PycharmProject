from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    cover_image_url = models.URLField(max_length=200, null=True, blank=True)
    summary = models.TextField()

    def __str__(self):
        return self.title
