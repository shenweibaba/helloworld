from django.shortcuts import render
from useradmin.models import *
# Create your views here.
def userindex(request):
    user = userInfo.objects.get(pk = 1)
    list = userInfo.objects.all()
    context = {'user':user,'userlist':list}
    return  render(request,'user/index.html',context=context)