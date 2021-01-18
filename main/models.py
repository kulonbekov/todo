from django.db import models



class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    is_closed = models.BooleanField(default = False)
    is_favorite = models.BooleanField(default = False)



class BookStore(models.Model):
    title = models.CharField(max_length = 100)
    subtitle = models.CharField(max_length = 200)
    description = models.CharField(max_length = 300)
    price = models.CharField(max_length = 50)
    genre = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    year = models.DateField()
    date = models.DateTimeField(auto_now_add = True)