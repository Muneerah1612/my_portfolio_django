from django.urls import path
from . import views
# this file is created so as to help activate views in the project urls.py by referencing this urls.py

urlpatterns = [
    path('',views.homepage,name = 'homepage'),
    path('<int:project_id>',views.detail,name = 'detail'),
]

