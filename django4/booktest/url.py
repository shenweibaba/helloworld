from django.contrib import admin
from django.urls import path,re_path
from  booktest import views
urlpatterns = [
    #path('<int:id>',views.queryBookById) # 关键字参数
    re_path('^([0-9]+)',views.queryBookById),
    path("getTest1",views.getTest1),
    path("getTest2",views.getTest2),
    path("getTest3",views.getTest3),
    path("cookies",views.cookieTest),
    path("toindex",views.toIndex),
    path("login",views.login),
    path("logout",views.logout),
    path("totest2",views.totest2)
]