from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home (request):

    peoples = [
        {'name' :'Sankalp','age':23},
        {'name' :'Shivam','age':28},
        {'name' :'Harsh','age':21},
        {'name' :'Rohan','age':13},
        {'name' :'Ranul','age':43}
    ]
    vegitable=["Tomato","carrot","cucumber"]

    text="hi I am Sanklap i love to watch movies and play games And bikes are the bret thing of thr world is his ideology "

    return render(request,"home/index.html", context={'peoples':peoples,'text':text,'vegitable':vegitable,'page':'Django toutorial 2024'})

def about(request):
    context={'page':'About'}
    return render(request,"home/about.html",context)



def contact(request):
    context={'page':'Contact'}
    return render(request,"home/contact.html",context)



def sucess_page(request):
    return HttpResponse("this is a sucess page ")


