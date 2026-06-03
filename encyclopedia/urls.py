from django.urls import path

from . import views
app_name= "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("random_page", views.random_page, name="random_page"),
    path("newpage", views.newpage, name="newpage"),
    path("created_page", views.created_page, name=
          "created_page"),
   
    
    path("<str:title>", views.entry, name="entry"),
    path("editpage/<str:title>", views.editpage, name="editpage")
]
