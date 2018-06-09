from django.shortcuts import render
from django.http import *
from  django.template import  RequestContext,loader #引入template包
from django.http import HttpResponseRedirect
from django.http.request import  *

# Create your views here.
from  booktest.models import *
def index(request):
    #加载模板
    bookList = Book.objects.all()[0:1] # 限制查询集
    bookTypeList = BookType.objects.all()[0:1]
    context = {'list':bookList,'bookTypes':bookTypeList}
    return HttpResponse(render(request,'booktest/index.html',context))

def queryBookById(request,id):
    bookType = BookType.objects.get(pk=id)
    print(bookType)
    booklist = bookType.book_set.all()
    print(booklist)
    return  HttpResponse(booklist)

def getTest1(request):
    A = request.GET.getlist('a')
    print(A)
    return  HttpResponse(render(request,"booktest/test1.html"))

#接收post请求的内容
def getTest2(request):
    HttpRequest
    return render(request,'booktest/test1.html')

def getTest3(request):
    name = request.POST['username']
    pwd = request.POST['password']
    context = {'name' : name , "pwd" : pwd}

    response  = HttpResponse()
    response.set_cookie("nihao","世界",180)
    return render(request, 'booktest/test2.html',context)

def cookieTest(request):
    response = HttpResponse()
    # response.set_cookie('123',"wordl",180)
    c = request.COOKIES['123']
    print(c)
    return response
def sessionTest(request):
    request.session.get('hello')
    pass

def toIndex(request):
    return  render(request,"booktest/login.html")

def login(request):
    name = request.POST['username']
    pwd = request.POST['password']
    context = {'name': name, "pwd": pwd}
    request.session['username'] = name
    return HttpResponseRedirect("/queryBookById/totest2")

def totest2(request):
    name = None
    if (request.session.has_key('username')):
        name = request.session['username']
    context = {'name' : name}
    return render(request,"booktest/test2.html",context)
#取消登录
def logout(request):
    if request.session.has_key('username'):
        del request.session['username']

    return  render(request,"booktest/login.html")