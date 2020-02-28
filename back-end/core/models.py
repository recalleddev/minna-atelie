from django.db import models

# Create your models here.

class Person(models.Model):
    SHIRT_SIZES = (
            ('s', 'small'),
            ('m', 'medium'),
            ('l', 'large'),
            )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    shirt_sizes = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        return self.first_name


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Publisher(models.Model):
    name = models.CharField(max_length=300)


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)


class Compra(models.Model):
    name = models.CharField(max_length=200)
    idade = models.CharField(max_length=10)

    def __str__(self):
        return self.nome