from django.urls import path,re_path
from  useradmin import userviews

urlpatterns = [
   path('index', userviews.userindex)
]