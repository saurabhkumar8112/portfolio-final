from django.shortcuts import render

def  index(request):
    return render(request,'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you want to contact me, kindly email me at','saurabhkumar8112@gmail.com']})
