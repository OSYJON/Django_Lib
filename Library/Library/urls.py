from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("", homepage),
    path("admin/", admin.site.urls),
    path("books/", include("Book.urls")),
    path("users/", include("Users.urls")),
    path("extend/", include("extend.urls")),
]