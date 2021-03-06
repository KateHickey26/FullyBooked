from django.urls import path
from fullybooked import views

# the below code imports the relevant django machinery for url mapping, and
# the views module from "fullybooked" app.
# This allows the function "url" to be called and point to the index view for mapping in "urlpatterns"
app_name = 'fullybooked'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_book/', views.add_book, name='add_book'),
    path('review_book/', views.review_book, name='review_book'),
]
