
from django.urls import path

from .views import blogView

urlpatterns = [
    path('', blogView),

]

