from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'ANJALI','age':12}
    return render(request,'data_render.html',context=d)


def conditions(request):
    d={'a':12,'b':25,'c':90}
    return render(request,'conditions.html',context=d)




