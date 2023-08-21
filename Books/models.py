from django.db import models

class books(models.Model):
    bookid = models.IntegerField(primary_key=True)
    bookname = models.CharField(max_length=10)
    book_author = models.CharField(max_length=50)




