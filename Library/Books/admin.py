from django.contrib import admin
from .models import BookDetails,PublisherDetails,CategoryDetails,LocationDetails

class Book_Details_Admin(admin.ModelAdmin):
    list_display = ["ID", "ISBN_Code", "Book_Title", "Language", "Binding_Id","No_Copies_Actual","No_Copies_Current","Category_id","Publication_year","Author_Id","Creation_Date","Comment","Borrower_able","IsRef"]

admin.site.register(BookDetails,Book_Details_Admin)
admin.site.register(PublisherDetails)
admin.site.register(CategoryDetails)
admin.site.register(LocationDetails)