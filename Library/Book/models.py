from django.db import models

class Publisher(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now=True)

class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_title = models.CharField(max_length=100)
    language = models.CharField(max_length=10)
    ISBN = models.IntegerField()
    is_ref = models.BooleanField(default=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

class CategoryDetails(models.Model):
    Category_Id = models.IntegerField(primary_key=True)
    Category_Name = models.CharField(max_length=50)
    Creation_Date = models.IntegerField()
    Comment = models.CharField(max_length=20)

    def __str__(self):
        return self.Category_Name

class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    shelf_number = models.IntegerField()
    shelf_floor = models.IntegerField()
    corridor = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now=True)