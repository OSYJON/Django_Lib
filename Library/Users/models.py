from django.db import models
from django.contrib.auth.models import User
from Books.models import BookDetails

class BorrowerDetails(models.Model):
    Borrow_Id = models.IntegerField(primary_key=True)
    Book_Id = models.ForeignKey(BookDetails, on_delete=models.CASCADE)
    Student_ID = models.IntegerField()
    Borrowed_From = models.DateTimeField()
    Borrowed_TO = models.DateTimeField()
    Actual_Return_Date = models.DateTimeField(null=True, blank=True)
    Issued_by = models.IntegerField()

    def __str__(self):
        return f"Borrow ID: {self.Borrow_Id}, Book ID: {self.Book_Id}, Student ID: {self.Student_ID}"

class StudentDetails(models.Model):
    Student_Id = models.CharField(max_length=10, primary_key=True)
    Student_Name = models.CharField(max_length=50)
    Sex = models.CharField(max_length=20)
    Date_Of_Birth = models.DateTimeField()
    Grade = models.CharField(max_length=10)
    Mobile_Number = models.CharField(max_length=11)
    Address = models.TextField()
    Email = models.EmailField()

    def __str__(self):
        return self.Student_Name