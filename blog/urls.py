from django.urls import path
from .views import index

app_name = "blog"

urlpatterns = [
    path('blog', index, name='list')
]
