from django.db import models

class BookDetails(models.Model):
    ID = models.IntegerField(primary_key=True)
    ISBN_Code = models.IntegerField()
    Book_Title = models.CharField(max_length=100)
    Language = models.CharField(max_length=10)
    Binding_Id = models.IntegerField()
    No_Copies_Actual = models.IntegerField()
    No_Copies_Current = models.IntegerField()
    Category_id = models.IntegerField()
    Publication_year = models.IntegerField()
    Author_Id = models.IntegerField()
    Creation_Date = models.IntegerField()
    Comment = models.CharField(max_length=255)
    Borrower_able = models.BooleanField()
    IsRef = models.IntegerField()

    def __str__(self):
        return self.Book_Title

class PublisherDetails(models.Model):
    Creation_Date = models.IntegerField()
    Binding_id = models.IntegerField(primary_key=True)
    Binding_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Binding_Name

class CategoryDetails(models.Model):
    Category_Id = models.IntegerField(primary_key=True)
    Category_Name = models.CharField(max_length=50)
    Creation_Date = models.IntegerField()
    Comment = models.CharField(max_length=20)

    def __str__(self):
        return self.Category_Name

class LocationDetails(models.Model):
    Shelf_id = models.IntegerField(primary_key=True)
    Shelf_No = models.IntegerField()
    Floor_No = models.IntegerField()
    Corridor = models.CharField(max_length=1)

    def __str__(self):
        return f"Shelf {self.Shelf_No}, Floor {self.Floor_No}, Corridor {self.Corridor}"