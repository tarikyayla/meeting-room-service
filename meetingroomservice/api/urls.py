from django.urls import path
from . import views 

urlpatterns = [
    path('availablerooms',views.get_availablerooms),
    path('bookroom',views.bookroom)
]
