from django.urls import path
from shop import views
urlpatterns = [
    path("", views.contact),
    path("tovar/", views.tovar),

]