# i created this file -gyan

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
 
def uppercase(request):
    text=request.GET.get('text','default')
    upperchar=text.upper()
    data={
        'upper_case':upperchar
    }
    return render(request, 'uppercase.html', data)

def charcount(request):
    text=request.GET.get('text','default')
    char='''`1234567890-=qwertyuiop[\]asdfghjkl;zxcvbnm,./~!@#$%^&*()_+}{|:"<>?QWERTYUIOPASDFGHJKLZXCVBNM'''
    char=set(char)
    data={
        'count':0
    }
    for i in text:
        if i in char:
            data['count']+=1
    return render(request, 'countchar.html', data)

def about(request):
    return render(request, 'about.html')

def removepucn(request):
    string=request.GET.get('text', 'default')
    s='qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
    s=set(s)
    new_string=''
    for i in string:
        if i in s:
            new_string+=i
    data={
        'text':new_string
    }
    return render(request, 'index.html', data)
